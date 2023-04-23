from rest_framework import serializers

from ads.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryRetrieveSerializer(CategoryListSerializer):
    pass


class CategoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class CategoryDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',)
