"""View module for handling requests for reservation data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Reservation


class ReservationView(ViewSet):
    """Honey Rae API reservations view"""

    def list(self, request):
        """Handle GET requests to get all reservations

        Returns:
            Response -- JSON serialized list of reservations
        """

        if request.auth.user.is_staff:
            reservations = Reservation.objects.filter(host=request.auth.user)
        else:
            reservations = Reservation.objects.filter(guest=request.auth.user)
        serialized = ReservationSerializer(reservations, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single reservation

        Returns:
            Response -- JSON serialized reservation record
        """

        reservation = Reservation.objects.get(pk=pk)
        serialized = ReservationSerializer(reservation, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ReservationSerializer(serializers.ModelSerializer):
    """JSON serializer for reservations"""
    class Meta:
        model = Reservation
        fields = ('year', 'make', 'model', 'color', 'odometer', 'capacity', 'chauffeured', 'owner')
        depth = 1