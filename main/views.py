from rest_framework.generics import CreateAPIView
from simple_login.views import (
    AccountActivationAPIView,
    RequestActivationKey,
    LoginAPIView,
    RetrieveUpdateDestroyProfileView,
)

from main.models import User
from main.serializers import UserSerializer


class Register(CreateAPIView):
    serializer_class = UserSerializer


class ActivateAccount(AccountActivationAPIView):
    user_model = User
    serializer_class = UserSerializer


class RequestUserActivationKey(RequestActivationKey):
    user_model = User


class UserDetails(RetrieveUpdateDestroyProfileView):
    user_model = User
    serializer_class = UserSerializer


class Login(LoginAPIView):
    user_model = User
    serializer_class = UserSerializer
