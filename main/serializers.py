from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from main.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile_phone = serializers.CharField(required=True)
    home_phone = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'home_phone',
            'mobile_phone',
        )
