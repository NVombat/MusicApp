from django.urls import path
from .views import Upload

urlpatterns = [
    path("upload", Upload.as_view()),
]
