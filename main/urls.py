from django.conf.urls import url

from main import views as main_views


urlpatterns = [
    url(r'^api/register$', main_views.Register.as_view()),
    url(r'^api/activate$', main_views.ActivateAccount.as_view()),
    url(r'^api/me$', main_views.UserDetails.as_view()),
    url(r'^api/login$', main_views.Login.as_view()),
    url(
        r'^api/request-activation-key$',
        main_views.RequestUserActivationKey.as_view()
    ),
    url(r'^api/properties$', main_views.ListCreateProperty.as_view()),
    url(
        r'^api/properties/(?P<pk>\d+)$',
        main_views.RetrieveUpdateDestroyProperty.as_view()
    ),
    url(r'^api/services$', main_views.ListCreateServiceRequest.as_view()),
    url(
        r'^api/services/active$',
        main_views.RetrieveActiveServiceRequests.as_view()
    ),
    url(r'^api/services/history', main_views.ServiceHistory.as_view()),
    url(
        r'^api/services/(?P<pk>\d+)$',
        main_views.RetrieveUpdateDestroyServiceRequest.as_view()
    ),
]
