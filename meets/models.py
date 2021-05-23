from django.db import models

# Create your models here.
class meet (models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class attendances(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    meet_id = models.ForeignKey(meet, on_delete=models.CASCADE, related_name="Attendances")
    fullname = models.CharField(max_length=255)