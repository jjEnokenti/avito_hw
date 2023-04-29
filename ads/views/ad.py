from django.db.models import Q
from django.http import JsonResponse
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response

from ads.models import Ad
from ads.serializers.ad import (
    AdCreateSerializer,
    AdUpdateSerializer,
    AdListSerializer, AdDestroySerializer, AdRetrieveSerializer
)


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def list(self, request, *args, **kwargs):
        cat = request.query_params.get('cat')
        text = request.query_params.get('text')
        location = request.query_params.get('location')
        price_from = request.query_params.get('price_from')
        price_to = request.query_params.get('price_to')

        filters = None

        if cat:
            if filters is None:
                filters = Q(category__exact=cat)
            else:
                filters &= Q(category__exact=cat)
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
