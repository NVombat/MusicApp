from django.urls import path
from .views import Upload

urlpatterns = [
    path("upload", Upload, Upload.as_view()),
]
