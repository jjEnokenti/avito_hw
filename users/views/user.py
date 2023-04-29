from django.db.models import Count, Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDestroySerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset().prefetch_related('locations').annotate(
            total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username'), many=True)

        response = self.get_paginated_response(self.paginate_queryset(serializer.data))
        response.data['items'] = response.data.pop('results')
        response.data['total'] = response.data.pop('count')
        response.data['num_pages'] = response.data['total'] // self.paginator.page_size

        return Response(response.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.queryset = User.objects.filter(id=pk).prefetch_related('locations').annotate(
            total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')

        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = UserUpdateSerializer

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.serializer_class = UserUpdateSerializer

        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.serializer_class = UserDestroySerializer

        return super().destroy(request, *args, **kwargs)
