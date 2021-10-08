from django.urls import path
from .views import Data

urlpatterns = [
    path("data", Data.as_view()),
]
