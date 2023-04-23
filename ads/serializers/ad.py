from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author_id',
            'author_name',
            'price',
            'description',
            'image',
            'is_published',
            'category_id',
            'category_name',
        )


class AdRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author_id',
            'author_name',
            'price',
            'description',
            'image',
            'is_published',
            'category_id',
            'category_name',
        )


class AdCreateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author',
            'author_name',
            'price',
            'description',
            'image',
            'is_published',
            'category',
            'category_name',
        )


class AdUpdateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False)

    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author',
            'author_name',
            'price',
            'description',
            'image',
            'is_published',
            'category',
            'category_name',
        )


class AdImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = (
            'id',
            'name',
            'author',
            'author_name',
            'price',
            'description',
            'image',
            'is_published',
            'category',
            'category_name',
        )


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id',)
