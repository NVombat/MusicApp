from .views import AdminView, AdminLogin, GenerateTokens
from django.urls import path

urlpatterns = [
    path("", AdminView.as_view()),
    path("login", AdminLogin.as_view()),
    path("generatetokens", GenerateTokens.as_view()),
]
