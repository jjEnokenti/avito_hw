from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from ads.models import Ad
from ads.serializers.ad import (
    AdCreateSerializer,
    AdSerializer,
    AdUpdateSerializer
)


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def list(self, request, *args, **kwargs):
        cat = request.query_params.get('cat')
        text = request.query_params.get('text')
        location = request.query_params.get('location')
        price_from = request.query_params.get('price_from')
        price_to = request.query_params.get('price_to')

        filters = None

        if cat:
            if filters is None:
                filters = Q(category=cat)
            else:
                filters &= Q(category=cat)
        if text:
            if filters is None:
                filters = Q(name__icontains=text)
            else:
                filters &= Q(name__icontains=text)
        if location:
            if filters is None:
                filters = Q(author__locations__name__icontains=location)
            else:
                filters &= Q(author__locations__name__icontains=location)
        if price_from:
            if filters is None:
                filters = Q(price__gte=price_from)
            else:
                filters &= Q(price__gte=price_from)
        if price_to:
            if filters is None:
                filters = Q(price__lte=price_to)
            else:
                filters &= Q(price__lte=price_to)

        queryset = self.get_queryset().select_related(
            'author').select_related(
            'category').order_by(
            '-price', 'name')

        if filters:
            serializer = self.get_serializer(queryset.filter(filters), many=True)
            response = self.get_paginated_response(self.paginate_queryset(serializer.data))
        else:
            serializer = self.get_serializer(queryset, many=True)
            response = self.get_paginated_response(self.paginate_queryset(serializer.data))

        response.data['items'] = response.data.pop('results')

        return Response(response.data)

    def create(self, request, *args, **kwargs):
        self.serializer_class = AdCreateSerializer

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = AdUpdateSerializer

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.serializer_class = AdUpdateSerializer

        return super().partial_update(request, *args, **kwargs)
