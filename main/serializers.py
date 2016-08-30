from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from np_assist_service.main.models import Property, Service, User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile_phone = serializers.CharField(required=True)
    home_phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'home_phone',
            'mobile_phone',
        )


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'owner',
            'address',
            'postcode',
            'category_primary',
            'category_secondary',
            'age',
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'site',
            'status',
            'description',
            'purpose',
            'paid_for',
            'requester_email',
            'address',
            'phone_number',
        )
