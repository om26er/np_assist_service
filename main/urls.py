from django.conf.urls import url

from rest_framework.authtoken import views

from main import views as main_views


urlpatterns = [
    url(r'^api/register$', main_views.UserRegistrationView.as_view()),
    url(r'^api/activate', main_views.UserActivationView.as_view()),
    url(r'^api/me', main_views.UserDetailsView.as_view()),
    url(r'^api/login$', views.obtain_auth_token),
]
