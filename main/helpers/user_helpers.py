from rest_framework.authtoken.models import Token

from main.models import User
from main.serializers import UserSerializer


ACTIVATION_KEY_DEFAULT = int(-1)


class UserHelpers:
    def __init__(self, **kwargs):
        self.user = User.objects.get(**kwargs)

    def is_active(self):
        return self.user.is_active

    def is_activation_key_valid(self, key):
        if int(key) == ACTIVATION_KEY_DEFAULT:
            return False
        return self.user.activation_key == int(key)

    def activate(self):
        if not self.user.is_active:
            self.user.is_active = True
            self.user.activation_key = ACTIVATION_KEY_DEFAULT
            self.user.save()

    def get_auth_token(self):
        return Token.objects.get(user_id=self.user.id).key

    def get_serialized_data(self):
        return UserSerializer(self.user).data

    def get_serialized_data_with_auth_token(self):
        data = self.get_serialized_data()
        data.update({'token': self.get_auth_token()})
        return data
