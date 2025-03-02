from django.db import models

class SpiritualEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    faith = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    organizer = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
