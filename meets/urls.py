from django.urls import path
from .api import MeetCreateApi, MeetListApi, MeetUpdateApi, MeetDeleteApi

urlpatterns = [
    path('api/create', MeetCreateApi.as_view()),
    path('api', MeetListApi.as_view()),
    path('api/<int:pk>', MeetUpdateApi.as_view()),
    path('api/<int:pk>/delete',MeetDeleteApi.as_view()),
]