from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.serializers import (
    ProfileSerializer,
    UserRegisterSerializer,
    UserReadSerializer,
    ChangePasswordSerializer,
    UserUpdateSerializer,
)


class UserProfile(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserRegister(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserReadSerializer

        return UserUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(UserReadSerializer(instance).data)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    model = get_user_model()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            return Response(
                {"detail": "Password updated successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
