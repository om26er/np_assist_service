from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from main.models import User
from main.helpers.user_helpers import UserHelpers
from main.helpers.response_helpers import ResponseConstructor
from main.permissions import IsOwner
from main.serializers import UserSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer


class UserActivationView(APIView):
    serializer_class = UserSerializer

    def _validate_parameters(self, email, activation_key):
        response_constructor = ResponseConstructor()
        response_constructor.validate_field('email', email)
        response_constructor.validate_field('activation_key', activation_key)
        return response_constructor.get_response()

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        activation_key = request.data.get('activation_key')
        message = self._validate_parameters(email, activation_key)
        if message:
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_account = UserHelpers(email)
            if user_account.is_active():
                return Response(
                    data={'email': ['Account already active.']},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not user_account.is_activation_key_valid(activation_key):
                return Response(
                    data={'activation_key': ['Invalid.']},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user_account.activate()
            return Response(
                data=user_account.get_serialized_data_with_auth_token(),
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                data={'email': ['Invalid email address.']},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserDetailsView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        try:
            user_account = UserHelpers(id=self.request.user.id)
            return Response(
                data=user_account.get_serialized_data(),
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
