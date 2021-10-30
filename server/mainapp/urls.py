from .views import Profile, Uploads, Posts
from django.urls import path

urlpatterns = [
    path("uploads", Uploads.as_view()),
    path("posts", Posts.as_view()),
    path("profile", Profile.as_view()),
]
