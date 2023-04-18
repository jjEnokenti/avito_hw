from rest_framework import serializers

from ads.models import Ad, Category


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Ad
        fields = ['id',
                  'name',
                  'author_id',
                  'author',
                  'price',
                  'description',
                  'image',
                  'is_published',
                  'category_id',
                  'category']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
