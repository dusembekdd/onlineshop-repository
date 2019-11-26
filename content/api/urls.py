from django.urls import path
from content.api.views import (
    all,
    listView,
)

app_name = 'content'
urlpatterns = [
    path('<int:pk>', all.api_homePage, name='homepage'),
    path('lists', listView.as_view(), name='list'),
]