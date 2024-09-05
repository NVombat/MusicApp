from django.urls import path

from .views import Contact_Us, Posts, Uploads

urlpatterns = [
    path("uploads", Uploads.as_view()),
    path("posts", Posts.as_view()),
    path("contactus", Contact_Us.as_view()),
]
