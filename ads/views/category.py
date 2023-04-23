from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from ads.models import Category
from ads.serializers.category import (
    CategoryListSerializer,
    CategoryDestroySerializer,
    CategoryUpdateSerializer,
    CategoryRetrieveSerializer,
    CategoryCreateSerializer
)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDestroySerializer
