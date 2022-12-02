from django.db import models

class Rental(models.Model):
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    pickUp = models.DateField
    startFuel = models.DecimalField
    dropOff = models.DateField
    newOdometer = models.IntegerField
    endFuel = models.DecimalField
    totalCost = models.IntegerField