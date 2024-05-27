import requests
import json

from django.utils.dateparse import parse_datetime
from django.utils import timezone as django_timezone

from datetime import timezone

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from core.models import SiteConfiguration, AccreditationStatus, PowerBiToken, ReportId
from core.serializers import SiteConfigurationSerializer

from pgob_auth.permissions import IsAdmin, IsReviewer

from pgob.settings import POWERBI_CLIENT_ID, POWERBI_CLIENT_SECRET, POWERBI_TENANT_ID

from datetime import datetime

from accreditations.views import AccreditationViewSet, ComplexAccreditationViewSet


class SiteConfigurationView(RetrieveUpdateAPIView):
    serializer_class = SiteConfigurationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdmin()]

    def get_object(self):
        return SiteConfiguration.objects.first()


class ReviewAccreditationBase(APIView):
    model = None
    serializer_class = None
    permission_classes = [IsAuthenticated & IsReviewer]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = self.model.objects.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except self.model.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RetrievePowerBiToken(APIView):
    permission_classes = [IsAuthenticated]

    def build_embed_url(self, group_id, report_id, embed_token):
        return f'https://app.powerbi.com/reportEmbed?reportId={report_id}&groupId={group_id}&w=2&config={embed_token}'

    def get_embed_token(self, access_token):
        url = "https://api.powerbi.com/v1.0/myorg/groups/76789884-6d41-48a4-a09a-2004737d536e/reports/2a3fa927-5ba8-4e81-ac4a-af0ef302e319/GenerateToken"

        data = {
            "accessLevel": "View",
            "datasetId": "6c3a1803-260d-4a23-8895-161079b9814b"
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()

    def save_token(self, access_token, expiration):
        expiration_date = parse_datetime(expiration)
        expiration_date = expiration_date.replace(tzinfo=timezone.utc)
        token, created = PowerBiToken.objects.get_or_create(
            token=access_token, expiration_date=expiration_date)
        return token

    def generate_token(self):
        data = {
            'grant_type': 'client_credentials',
            'client_secret': POWERBI_CLIENT_SECRET,
            'client_id': POWERBI_CLIENT_ID,
            'resource': 'https://analysis.windows.net/powerbi/api'
        }

        get_token_request = requests.post(
            url=f'https://login.microsoftonline.com/{
                POWERBI_TENANT_ID}/oauth2/token',
            data=data
        )

        response = json.loads(get_token_request.text)
        access_token = response.get('access_token')

        embed_data = self.get_embed_token(access_token)
        expiration_date = embed_data.get('expiration')

        self.save_token(embed_data.get('token'), expiration_date)
        return access_token.split('.')[0]

    def get(self, request: Request):

        token_instance = PowerBiToken.objects.last()
        now = django_timezone.make_aware(datetime.now(), timezone.utc)
        access_token = None

        if token_instance is None:
            access_token = self.generate_token()
        else:
            if token_instance.expiration_date < now:
                access_token = self.generate_token()

        token_instance = PowerBiToken.objects.last()
        # embed_token = token_instance.token.split('.')[0]
        embed_url = self.build_embed_url('76789884-6d41-48a4-a09a-2004737d536e',
                                         '2a3fa927-5ba8-4e81-ac4a-af0ef302e319', access_token)

        # print(token_instance.expiration_date, now)

        return Response({
            'token': token_instance.token,
            'embed_url': embed_url
        })
