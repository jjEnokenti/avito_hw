from rest_framework import serializers

from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserDetailSerializer(UserListSerializer):
    pass


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserUpdateSerializer(serializers.ModelSerializer):
    pass
