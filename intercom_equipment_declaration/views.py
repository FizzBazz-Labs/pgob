from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from intercom_equipment_declaration.models import IntercomEquipmentDeclaration
from intercom_equipment_declaration.serializers import IntercomEquipmentDeclarationSerializer

from core.models import AccreditationStatus
from core.views import ReviewAccreditationBase, AccreditationViewSet

from pgob_auth.permissions import IsReviewer, IsAccreditor


class IntercomEquipmentDeclarationViewSet(AccreditationViewSet):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    filterset_fields = ['status', 'country']


class IntercomEquipmentDeclarationListApiView(ListCreateAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer
    permission_classes = [IsAuthenticated]


class IntercomEquipmentDeclarationRetrieveApiView(RetrieveUpdateAPIView):
    queryset = IntercomEquipmentDeclaration.objects.all()
    serializer_class = IntercomEquipmentDeclarationSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAuthenticated()]


class ReviewAccreditation(ReviewAccreditationBase):
    model = IntercomEquipmentDeclaration
    serializer_class = IntercomEquipmentDeclarationSerializer


class ApproveAccreditation(APIView):
    serializer_class = IntercomEquipmentDeclarationSerializer
    permission_classes = [IsAuthenticated & IsAccreditor]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = IntercomEquipmentDeclaration.objects.get(pk=pk)
            item.status = AccreditationStatus.APPROVED
            item.authorized_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except IntercomEquipmentDeclaration.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RejectAccreditation(APIView):
    serializer_class = IntercomEquipmentDeclarationSerializer
    permission_classes = [IsAuthenticated & (IsReviewer | IsAccreditor)]

    def patch(self, request: Request, pk, *args, **kwargs):
        try:
            item = IntercomEquipmentDeclaration.objects.get(pk=pk)
            item.status = AccreditationStatus.REJECTED
            item.rejected_by = request.user
            item.save()

            serializer = self.serializer_class(item)
            return Response(serializer.data, status=HTTP_200_OK)

        except IntercomEquipmentDeclaration.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
