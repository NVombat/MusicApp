from django.urls import path

from .views import Profile

urlpatterns = [
    path("profile", Profile.as_view()),
]
