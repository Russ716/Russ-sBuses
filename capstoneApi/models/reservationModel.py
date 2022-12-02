from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    guest = models.ForeignKey("Guest", on_delete=models.CASCADE)
    bus = models.ForeignKey("Bus", on_delete=models.CASCADE)
    owner = models.ForeignKey("Host", on_delete=models.CASCADE)
    reserveStart = models.DateField
    reserveNights = models.IntegerField
    estimateCost = models.IntegerField