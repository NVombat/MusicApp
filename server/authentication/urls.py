from .views import Register, Login, ResetPassword, ResetPasswordLink
from django.urls import path

urlpatterns = [
    path("register", Register.as_view()),
    path("login", Login.as_view()),
    path("resetpwd", ResetPassword.as_view()),
    path("resetlink", ResetPasswordLink.as_view()),
]
