from rest_framework import  serializers
from .models import meet

class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = meet
        fields = '__all__'