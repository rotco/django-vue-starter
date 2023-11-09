from django.urls import path
from .views import *

urlpatterns = [path("items", ItemList.as_view())]
