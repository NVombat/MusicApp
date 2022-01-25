from .views import AdminView, AdminLogin
from django.urls import path

urlpatterns = [
    path("", AdminView.as_view()),
    path("login", AdminLogin.as_view()),
]
