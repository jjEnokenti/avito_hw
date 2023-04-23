from django.db.models import Count, Q
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveAPIView
)

from users.models import User
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDestroySerializer,
    UserRetrieveSerializer
)


class UserListView(ListAPIView):
    queryset = User.objects.prefetch_related('locations').annotate(
        total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')
    serializer_class = UserListSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.prefetch_related('locations').annotate(
        total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')
    serializer_class = UserRetrieveSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
