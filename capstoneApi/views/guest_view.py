"""View module for handling requests for guest data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Guest


class GuestView(ViewSet):
    """Honey Rae API guests view"""

    def list(self, request):
        """Handle GET requests to get all guests

        Returns:
            Response -- JSON serialized list of guests
        """

        guests = Guest.objects.all()
        serialized = GuestSerializer(guests, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single guest

        Returns:
            Response -- JSON serialized guest record
        """

        guest = Guest.objects.get(pk=pk)
        serialized = GuestSerializer(guest, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class GuestSerializer(serializers.ModelSerializer):
    """JSON serializer for guests"""
    class Meta:
        model = Guest
        fields = ('id', 'user', 'mileageTraveled')