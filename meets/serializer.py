from rest_framework import  serializers
from .models import meet, attendances

#http://www.tomchristie.com/rest-framework-2-docs/api-guide/relations#nested-relationships


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendances
        fields = ('fullname', 'attendance_id' )

class MeetSerializer(serializers.ModelSerializer):

    Attendances = AttendanceSerializer(many=True)

    def create(self, validated_data):
        attendances_data = validated_data.pop('Attendances')
        meet_ = meet.objects.create(**validated_data)
        for att_data in attendances_data:
            attendances.objects.create(meet_id=meet_, **att_data)
        return meet_
    
    def update(self, instance, validated_data):
        attendances_data = validated_data.pop('Attendances')
        meet.objects.filter(id=instance.id).update(**validated_data)
        for att_data in attendances_data:
            attendances.objects.get_or_create(meet_id=instance, **att_data)
        return instance
  
    class Meta:
        model = meet
        fields = '__all__'
