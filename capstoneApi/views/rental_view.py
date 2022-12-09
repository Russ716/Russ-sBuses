"""View module for handling requests for rental data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Rental, Reservation


class RentalView(ViewSet):
    """Honey Rae API rentals view"""

    def list(self, request):
        """Handle GET requests to get all rentals

        Returns:
            Response -- JSON serialized list of rentals
        """

        if request.auth.user.is_staff:
            rentals = Rental.objects.filter(host=request.auth.user)
        else:
            rentals = Rental.objects.filter(guest=request.auth.user)
        serialized = RentalSerializer(rentals, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single rental

        Returns:
            Response -- JSON serialized rental record
        """

        rental = Rental.objects.get(pk=pk)
        serialized = RentalSerializer(rental, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """POST request for creating Bus object"""
        reservation = Reservation.objects.get(pk=request.data["reservation"])
        
        new_rental = Rental()
        new_rental.reservation = reservation
        new_rental.pickUp = request.data["pickUp"]
        new_rental.startFuel = request.data["startFuel"]
        new_rental.dropOff = request.data["dropOff"]
        new_rental.newOdometer = request.data["newOdometer"]
        new_rental.endFuel = request.data["endFuel"]
        new_rental.totalCost = request.data["totalCost"]
        new_rental.save()
        
        serialized = RentalSerializer(new_rental, many = False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class RentalSerializer(serializers.ModelSerializer):
    """JSON serializer for rentals"""
    class Meta:
        model = Rental
        fields = ('reservation', 'pickUp', 'startFuel', 'dropOff', 'newOdometer', 'endFuel', 'totalCost')
        depth = 1
