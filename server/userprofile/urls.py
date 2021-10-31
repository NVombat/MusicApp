from .views import Profile
from django.urls import path

urlpatterns = [
    path("profile", Profile.as_view()),
]