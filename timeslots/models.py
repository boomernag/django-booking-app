from django.db import models

# Create your models here.
    
class TimeSlot(models.Model):
    number_of_possible_bookings = models.PositiveIntegerField()
    is_slot_available = models.CharField(max_length=1,choices=CHOICES)
    is_slot_full = models.CharField(max_length=1, choices=CHOICES)
