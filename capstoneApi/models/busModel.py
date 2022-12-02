from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    year = models.PositiveSmallIntegerField
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    odometer = models.PositiveSmallIntegerField
    capacity = models.PositiveSmallIntegerField
    chauffeured = models.BooleanField
    owner = models.ForeignKey(User, on_delete=models.CASCADE)