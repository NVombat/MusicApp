from .views import Test, Uploads, Posts
from django.urls import path

urlpatterns = [
    path("uploads", Uploads.as_view()),
    path("posts", Posts.as_view()),
    path("test", Test.as_view()),
]
