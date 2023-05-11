from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ads.permissions import CanEditOrDelete
from ads.filters import AdFilter
from ads.models import Ad
from ads.serializers.ad import (
    AdSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdDestroySerializer,
)


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    serializers = {
        "update": AdUpdateSerializer,
        "partial_update": AdUpdateSerializer,
        "create": AdCreateSerializer,
        "destroy": AdDestroySerializer
    }

    default_permission = [IsAuthenticated, CanEditOrDelete]
    permissions = {
        'list': [],
        'retrieve': [IsAuthenticated],
        "create": [IsAuthenticated]
    }

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().select_related(
            'author').select_related(
            'category').order_by(
            '-price', 'name')

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().select_related(
            'author').select_related(
            'category').all()

        return super().retrieve(request, *args, **kwargs)
