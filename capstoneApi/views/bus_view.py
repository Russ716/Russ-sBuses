"""View module for handling requests for bus data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Bus


class BusView(ViewSet):
    """Honey Rae API buses view"""

    def list(self, request):
        """Handle GET requests to get all buses

        Returns:
            Response -- JSON serialized list of buses
        """

        buses = Bus.objects.all()
        serialized = BusSerializer(buses, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single bus

        Returns:
            Response -- JSON serialized bus record
        """

        bus = Bus.objects.get(pk=pk)
        serialized = BusSerializer(bus, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class BusSerializer(serializers.ModelSerializer):
    """JSON serializer for buses"""
    class Meta:
        model = Bus
        fields = ('year', 'make', 'model', 'color', 'odometer', 'capacity', 'chauffeured', 'owner')