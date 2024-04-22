from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pgob_auth.serializers import ChangePasswordSerializer


class ChangePasswordView(UpdateAPIView):
    model = get_user_model()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        self.object.set_password(serializer.data.get("password"))
        self.object.save()

        return Response("Success.", status=status.HTTP_200_OK)
