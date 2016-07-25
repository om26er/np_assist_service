from django.conf.urls import url

from main import views as main_views


urlpatterns = [
    url(r'^api/register$', main_views.Register.as_view()),
    url(r'^api/activate$', main_views.ActivateAccount.as_view()),
    url(r'^api/me$', main_views.UserDetails.as_view()),
    url(r'^api/login$', main_views.Login.as_view()),
]
