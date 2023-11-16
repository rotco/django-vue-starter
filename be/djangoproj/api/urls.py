from django.urls import path
from .views import *

urlpatterns = [
    path("users", UserList.as_view()),
    path("users/<pk>/delete", UserDeleteView.as_view()),
]
