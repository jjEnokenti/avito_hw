from rest_framework import serializers

from ads.models import Ad
from ads.serializers.validators import IsPublishedNotTrue
from users.serializers.user import UserAdSerializer


class AdSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


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
    is_published = serializers.BooleanField(default=False, validators=[IsPublishedNotTrue()])

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
