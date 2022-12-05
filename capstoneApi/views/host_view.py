"""View module for handling requests for host data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from capstoneApi.models import Host


class HostView(ViewSet):
    """Honey Rae API hosts view"""

    def list(self, request):
        """Handle GET requests to get all hosts

        Returns:
            Response -- JSON serialized list of hosts
        """

        hosts = Host.objects.all()
        serialized = HostSerializer(hosts, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single host

        Returns:
            Response -- JSON serialized host record
        """

        host = Host.objects.get(pk=pk)
        serialized = HostSerializer(host, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class HostSerializer(serializers.ModelSerializer):
    """JSON serializer for hosts"""
    class Meta:
        model = Host
        fields = ('id', 'user', 'rentalNumber')