from django.db import models
from datetime import time

# Create your models here.

class Meetings(models.Model):
    meeting_title = models.CharField(max_length=200)
    meeting_date = models.DateField() 
    
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    
    def __str__(self):
        return self.meeting_title
    
