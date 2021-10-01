from django.urls import path
from .views import UserLogin

urlpatterns = [
    path('login', UserLogin, UserLogin.as_view()),
]
