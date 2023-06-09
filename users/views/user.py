from django.db.models import Count, Q
from rest_framework import viewsets, generics

from ..models.user import User
from ..serializers.user import (
    UserBaseSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDestroySerializer
)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    default_serializer = UserBaseSerializer
    serializers = {
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
        "create": UserCreateSerializer,
        "destroy": UserDestroySerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().prefetch_related('locations').annotate(
            total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.queryset = User.objects.filter(id=pk).prefetch_related('locations').annotate(
            total_ads=Count('ads', filter=Q(ads__is_published=True)))

        return super().retrieve(request, *args, **kwargs)
