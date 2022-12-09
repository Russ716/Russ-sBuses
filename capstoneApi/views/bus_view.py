"""View module for handling requests for bus data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Bus, Host


class BusView(ViewSet):
    """Honey Rae API buses view"""

    def list(self, request):
        """Handle GET requests to get all buses

        Returns:
            Response -- JSON serialized list of buses
        """

        if request.auth.user.is_staff:
            buses = Bus.objects.filter(host=request.auth.user)
        else:
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
    
    def create(self, request):
        """POST request for creating Bus object"""
        new_bus = Bus()
        new_bus.year = request.data["year"]
        new_bus.make = request.data["make"]
        new_bus.model = request.data["model"]
        new_bus.color = request.data["color"]
        new_bus.odometer = request.data["odometer"]
        new_bus.capacity = request.data["capacity"]
        new_bus.chauffeured = request.data["chauffeured"]
        new_bus.owner = Host.objects.get(user=request.auth.user)
        new_bus.image = request.data["image"]
        new_bus.save()
        
        serialized = BusSerializer(new_bus, many = False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class BusOwnerSerializer(serializers.ModelSerializer):
    """JSON serializer for bus owners"""
    class Meta:
        model = Host
        fields = ('id', 'full_name', 'rentalNumber')

class BusSerializer(serializers.ModelSerializer):
    """JSON serializer for buses"""
    owner = BusOwnerSerializer(many=False)
    
    class Meta:
        model = Bus
        fields = ('year', 'make', 'model', 'color', 'odometer', 'capacity', 'chauffeured', 'owner', 'image')
        depth = 1