from django.http import JsonResponse
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ads.models import Ad
from ads.serializers.ad import (
    AdCreateSerializer,
    AdRetrieveSerializer,
    AdListSerializer,
    AdUpdateSerializer,
    AdDestroySerializer,
    AdImageUploadSerializer
)


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdView(ListAPIView):
    queryset = Ad.objects.select_related('author').select_related('category').order_by('-price', 'name').all()
    serializer_class = AdListSerializer


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
    serializer_class = AdImageUploadSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
