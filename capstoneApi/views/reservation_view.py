"""View module for handling requests for reservation data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Reservation, Guest, Host, Bus


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

    def create(self, request):
        """POST request for creating Bus object"""
        guest = Guest.objects.get(user=request.auth.user)
        bus = Bus.objects.get(pk=request.data["bus"])
        owner = Host.objects.get(user=request.auth.user)
        
        new_reservation = Reservation()
        new_reservation.owner = owner
        new_reservation.guest = guest
        new_reservation.bus = bus
        new_reservation.reserveStart = request.data["reserveStart"]
        new_reservation.reserveNights = request.data["reserveNights"]
        new_reservation.estimateCost = request.data["estimateCost"]
        new_reservation.save()
        
        serialized = ReservationSerializer(new_reservation, many = False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for a reservation

        Returns:
            Response -- Empty body with 204 status code
        """
        reservation = Reservation.objects.get(pk=pk)
        reservation.reserveStart = request.data["reserveStart"]
        reservation.reserveNights = request.data["reserveNights"]
        reservation.estimateCost = request.data["estimateCost"]
        reservation.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk=None):
        """Handle DELETE requests for a single reservation

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            reservation = Reservation.objects.get(pk=pk)
            reservation.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Reservation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReservationSerializer(serializers.ModelSerializer):
    """JSON serializer for reservations"""
    class Meta:
        model = Reservation
        fields = ('guest', 'bus', 'owner', 'reserveStart', 'reserveNights', 'estimateCost')
        depth = 1
        
