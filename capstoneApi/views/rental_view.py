"""View module for handling requests for rental data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Rental


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


class RentalSerializer(serializers.ModelSerializer):
    """JSON serializer for rentals"""
    class Meta:
        model = Rental
        fields = ('year', 'make', 'model', 'color', 'odometer', 'capacity', 'chauffeured', 'owner')
        depth = 1