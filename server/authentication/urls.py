from .views import Login, ResetPassword
from django.urls import path

urlpatterns = [
    path("login", Login.as_view()),
    path("resetpwd", ResetPassword.as_view()),
]
