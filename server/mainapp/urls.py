from .views import Contact_Us, Uploads, Posts
from django.urls import path

urlpatterns = [
    path("uploads", Uploads.as_view()),
    path("posts", Posts.as_view()),
    path("contactus", Contact_Us.as_view()),
]
