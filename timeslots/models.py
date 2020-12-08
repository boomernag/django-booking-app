from django.db import models

# Create your models here.

class TimeSlot(models.Model):
    timeslot_id = models.CharField(max_length=20)
    number_of_possible_bookings = models.PositiveIntegerField()
    is_slot_available = models.CharField(max_length=1)
    is_slot_full = models.CharField(max_length=1)

    def __str__(self):
        return self.timeslot_id
