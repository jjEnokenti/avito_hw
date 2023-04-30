from django_filters import rest_framework as f

from ads.models import Ad


class AdFilter(f.FilterSet):
    cat = f.NumberFilter(field_name="category", lookup_expr='exact')
    location = f.CharFilter(field_name="author__locations__name", lookup_expr='icontains')
    price_from = f.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = f.NumberFilter(field_name='price', lookup_expr='lte')
    text = f.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ['cat', 'location', 'price_from', 'price_to']
