from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


# class UserProfile(RetrieveAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user
