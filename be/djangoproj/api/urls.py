from django.urls import path
from .views import *

urlpatterns = [
    path("users", UserList.as_view(), name="users"),
    path("filtered-users", FilteredUserIds.as_view(), name="filtered-users"),
    path("users/<pk>/delete", UserDeleteView.as_view(), name="user-delete"),
]
