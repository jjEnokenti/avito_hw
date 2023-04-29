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


class AdRetrieveSerializer(AdListSerializer):
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
            'price',
            'description',
            'image',
            'is_published',
            'category',
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
            'price',
            'description',
            'image',
            'is_published',
            'category',
        )


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id',)
