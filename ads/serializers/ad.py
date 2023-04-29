from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
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
    pass


class AdCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
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
    image = serializers.ImageField(required=False)
    id = serializers.IntegerField(read_only=True)

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
