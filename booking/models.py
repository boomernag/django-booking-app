import uuid

from django.db import models
from datetime import datetime


# Create your models here.
class TimeSlotBooking(models.Model):
    customer_email = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.start_timestamp
