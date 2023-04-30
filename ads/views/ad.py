from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response

from ads.filter_class import AdFilter
from ads.models import Ad
from ads.serializers.ad import (
    AdCreateSerializer,
    AdUpdateSerializer,
    AdListSerializer, AdDestroySerializer, AdRetrieveSerializer
)


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdView(ListAPIView):
    queryset = Ad.objects.select_related(
        'author').select_related(
        'category').order_by(
        '-price', 'name')
    serializer_class = AdListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        response.data['items'] = response.data.pop('results')
        response.data['total'] = response.data.pop('count')
        response.data['num_pages'] = response.data['total'] // self.paginator.page_size

        return Response(response.data)


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdRetrieveView(RetrieveAPIView):
    queryset = Ad.objects.select_related('author').select_related('category').all()
    serializer_class = AdRetrieveSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdUploadImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
