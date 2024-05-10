from io import BytesIO
from http import HTTPMethod

import pandas as pd

from django.http import HttpResponse
from django.db.models.query import QuerySet

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from core import utils
from core.models import AccreditationStatus, SiteConfiguration, Certification

from credentials.utils import certificate_accreditation


class ApproveMixin:
    @action(detail=True, methods=['patch'])
    def approve(self, request: HttpResponse, pk: None, *args, **kwargs) -> Response:
        queryset: QuerySet = self.get_queryset()

        try:
            item = queryset.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.authorized_comment = request.data.get('authorized_comment')

            if 'type' in request.data:
                item.type = request.data.get('type')

            item.save()

            serializer = self.get_serializer_class()(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except queryset.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ReviewMixin:
    @action(detail=True, methods=['patch'])
    def review(self, request: Request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()

        try:
            item = queryset.get(pk=pk)
            item.status = AccreditationStatus.REVIEWED
            item.reviewed_by = request.user
            item.reviewed_comment = request.data.get('reviewed_comment')
            item.save()

            serializer = self.get_serializer_class()(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except queryset.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RejectMixin:
    @action(detail=True, methods=['patch'])
    def reject(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()

        try:
            item = queryset.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.get_serializer_class()(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except queryset.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CertificateMixin:
    @action(detail=True, methods=['patch'])
    def certificate(self, request: Request, pk=None, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        model = queryset.model

        configuration = SiteConfiguration.objects.filter(available=True).first()

        if not configuration:
            return Response(
                {"error": "Site not available."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        try:
            item = queryset.get(pk=pk)
            certificate_accreditation(configuration, 'nationals', item)

        except Certification.DoesNotExist:
            return Response(
                {"error": "Certification config not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except model.DoesNotExist:
            return Response(
                {"error": "National accreditation not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )


class ExportDataMixin:
    @action(detail=False,
            methods=[HTTPMethod.GET],
            permission_classes=[AllowAny])
    def export(self, request, *args, **kwargs) -> HttpResponse:
        queryset = self.get_queryset().filter(status=AccreditationStatus.PENDING)

        if not queryset.exists():
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        buffer = BytesIO()

        utils.get_data_frame(queryset=queryset) \
            .to_excel(buffer, index=False, sheet_name='Items')

        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

        response['Content-Disposition'] = 'attachment; filename=data.xlsx'

        return response


class ImportDataMixin:
    @action(detail=False,
            methods=[HTTPMethod.POST],
            url_path='import', url_name='import',
            permission_classes=[AllowAny])
    def import_data(self, request: Request, *args, **kwargs) -> Response:
        try:
            df = pd.read_excel(request.FILES['data'])
            df = df.rename(columns={'ID': 'id', 'Estado': 'status'})
            df['status'] = df['status'].str.lower()

        except KeyError:
            return Response(
                {"error": "Data file or columns not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        bulk_data = []
        queryset: QuerySet = self.get_queryset()

        for index, row in df.iterrows():
            try:
                item = queryset.get(pk=row['id'])

                match row['status']:
                    case 'revisado':
                        item.status = AccreditationStatus.REVIEWED
                    case 'rechazado':
                        item.status = AccreditationStatus.REJECTED
                    case _:
                        item.status = AccreditationStatus.PENDING

                bulk_data.append(item)

            except:
                continue

        queryset.bulk_update(bulk_data, ['status'])

        return Response(
            {"message": "Accepted"},
            status=status.HTTP_202_ACCEPTED,
        )
