from django.urls import path
from .views import *

urlpatterns = [
    path("resume/<resume_path>/", ResumeList.as_view()),
]
