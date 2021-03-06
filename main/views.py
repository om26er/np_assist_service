from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import permissions, response, status
from simple_login.views import (
    AccountActivationAPIView,
    RequestActivationKey,
    LoginAPIView,
    RetrieveUpdateDestroyProfileView,
)

from main.models import (
    Property,
    Service,
    User,
    SERVICE_ACTIVE_STATES,
    SERVICE_STATUS_DONE,
)
from main.serializers import (
    PropertySerializer,
    ServiceSerializer,
    UserSerializer,
)


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


class ListCreateProperty(ListCreateAPIView):
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data.update({'owner': self.request.user.id})
        return super().post(request, *args, **kwargs)


class RetrieveUpdateDestroyProperty(RetrieveUpdateDestroyAPIView):
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Property.objects.filter(
            id=self.kwargs['pk'],
            owner=self.request.user
        )

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=self.request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ListCreateServiceRequest(ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Service.objects.filter(site__owner=self.request.user)


class RetrieveUpdateDestroyServiceRequest(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Service.objects.filter(
            id=self.kwargs['pk'],
            site__owner=self.request.user
        )

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=self.request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveActiveServiceRequests(ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Service.objects.filter(
            site__owner=self.request.user,
            status__in=SERVICE_ACTIVE_STATES
        )


class ServiceHistory(ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Service.objects.filter(
            site__owner=self.request.user,
            status=SERVICE_STATUS_DONE
        )
