from django.urls import path
from .views import Uploads, Posts

urlpatterns = [
    path("uploads", Uploads.as_view()),
    path("posts", Posts.as_view()),
]
