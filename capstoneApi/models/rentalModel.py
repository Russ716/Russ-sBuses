from django.db import models

class Rental(models.Model):
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    pickUp = models.DateField()
    startFuel = models.DecimalField(max_digits=2, decimal_places=0)
    dropOff = models.DateField()
    newOdometer = models.IntegerField()
    endFuel = models.DecimalField(max_digits=2, decimal_places=0)
    totalCost = models.IntegerField()