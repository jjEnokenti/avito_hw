from rest_framework import viewsets
from rest_framework.response import Response

from users.models import Location
from users.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        response = self.get_paginated_response(self.paginate_queryset(serializer.data))
        response.data['items'] = response.data.pop('results')

        return Response(response.data)
