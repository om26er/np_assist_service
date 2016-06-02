from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework import permissions

from main.models import User
from main.permissions import IsOwner
from main.serializers import UserSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer


class UserActivationView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        pass


class UserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (
        IsOwner,
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
