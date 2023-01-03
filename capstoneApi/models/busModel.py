from django.db import models


class Bus(models.Model):
    year = models.PositiveSmallIntegerField()
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    odometer = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    chauffeured = models.BooleanField()
    owner = models.ForeignKey("Host", on_delete=models.CASCADE)
    image = models.CharField(max_length=256)
    
    @property
    def owner_name(self):
        return f'{self.owner.first_name} {self.owner.last_name}'