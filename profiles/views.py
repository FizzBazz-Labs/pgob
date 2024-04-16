from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from profiles.serializers import ProfileSerializer, UserRegisterSerializer, UserSerializer, UserReadSerializer


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


class UserDetailView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserReadSerializer
