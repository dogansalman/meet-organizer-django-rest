from rest_framework import generics
from rest_framework.response import Response
from .serializer import MeetSerializer, AttendanceSerializer
from .models import meet, attendances

class MeetCreateApi(generics.CreateAPIView):
    queryset = meet.objects.all()
    serializer_class = MeetSerializer

class MeetListApi(generics.ListAPIView):
    queryset = meet.objects.all()
    serializer_class = MeetSerializer

class MeetUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = meet.objects.all()
    serializer_class = MeetSerializer    

class MeetDeleteApi(generics.DestroyAPIView):
    queryset = meet.objects.all()
    serializer_class = MeetSerializer    

class AttendanceDeleteApi(generics.DestroyAPIView):
    queryset = attendances.objects.all()
    serializer_class = AttendanceSerializer    