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


class AdUpdateSerializer(AdCreateSerializer):
    id = serializers.IntegerField(read_only=True)


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id',)
