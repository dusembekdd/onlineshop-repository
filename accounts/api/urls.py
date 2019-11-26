from django.urls import path
from accounts.api.views import register_api

app_name= 'accounts'
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register', register_api, name='register'),
    path('login', obtain_auth_token, name='login')
]