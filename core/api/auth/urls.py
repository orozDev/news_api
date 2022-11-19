from django.urls import path, include
from .views import LoginApi


urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('', include('rest_registration.api.urls')),
]
