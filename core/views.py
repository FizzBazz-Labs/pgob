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

from core.models import SiteConfiguration, AccreditationStatus, PowerBiToken
from core.serializers import SiteConfigurationSerializer

from pgob_auth.permissions import IsAdmin, IsReviewer

from pgob.settings import POWERBI_CLIENT_ID, POWERBI_CLIENT_SECRET, POWERBI_TENANT_ID
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

    # def build_embed_url(self, group_id, report_id, embed_token):
    #     return f'https://app.powerbi.com/reportEmbed?reportId={report_id}&groupId={group_id}&w=2&config={embed_token}'

    def build_embed_url(self, group_id, report_id, access_token):
        url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/reports/{report_id}"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        embed_request = requests.get(url, headers=headers)
        response = json.loads(embed_request.text)
        return response


    def get_embed_token(self, access_token):
        url = "https://api.powerbi.com/v1.0/myorg/GenerateToken"

        data = {
            "reports": [
                {
                    "id": "116de701-d119-4ab8-962a-a07a906f45ac",
                },
                {
                    "id": "9e0162af-ec43-4457-8d9d-f992a0c9d78c",
                }
            ],
            "datasets": [
                {
                    "id": "0f821299-8a62-456f-93a2-5ec7b9fffb6f",
                    "xmlaPermissions": "ReadOnly"
                }
            ],
            "targetWorkspaces": [
                {
                    "id": "76789884-6d41-48a4-a09a-2004737d536e"
                }
            ]
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def save_token(self, token, expiration, access_token):
        expiration_date = expiration
        expiration_date = expiration_date.replace(tzinfo=timezone.utc)
        token, created = PowerBiToken.objects.get_or_create(
            token=token, expiration_date=expiration_date, access_token=access_token)
        return token

    def generate_token(self):
        now = django_timezone.now()
        data = {
            'grant_type': 'client_credentials',
            'client_secret': POWERBI_CLIENT_SECRET,
            'client_id': POWERBI_CLIENT_ID,
            'scope': 'https://analysis.windows.net/powerbi/api/.default'
        }

        get_token_request = requests.post(
            url=f'https://login.microsoftonline.com/{
                POWERBI_TENANT_ID}/oauth2/v2.0/token',
            data=data
        )

        response = json.loads(get_token_request.text)
        access_token = response.get('access_token')
        embed_data = self.get_embed_token(access_token)
        expiration_date = parse_datetime(embed_data.get('expiration'))
        self.save_token(embed_data.get('token'), expiration_date, access_token)

    def get(self, request: Request, report_id):

        token_instance = PowerBiToken.objects.last()
        now = django_timezone.now()

        if token_instance is None:
            self.generate_token()
        else:
            if token_instance.expiration_date < now:
                self.generate_token()

        token_instance = PowerBiToken.objects.last()

        embed_url = self.build_embed_url('76789884-6d41-48a4-a09a-2004737d536e',
                                         report_id, token_instance.access_token)

        return Response({
            'token': token_instance.token,
            'embed_url': embed_url,
            'repor_id': report_id
        })
