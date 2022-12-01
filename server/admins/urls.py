from django.urls import path

from .views import AdminLogin, AdminView, GenerateTokens

urlpatterns = [
    path("", AdminView.as_view()),
    path("login", AdminLogin.as_view()),
    path("generatetokens", GenerateTokens.as_view()),
]
