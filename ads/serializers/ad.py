from rest_framework import serializers

from ads.models import Ad
from users.serializers import UserAdSerializer


class AdSerializer(serializers.ModelSerializer):
    author = UserAdSerializer()
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

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
