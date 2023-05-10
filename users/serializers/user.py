from rest_framework import serializers

from ..models.location import Location
from ..models.user import User


class UserBaseSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ('password',)


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
            'password': {'write_only': True}
        }

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.get('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if self._locations:
            for location in self._locations:
                loc_obj, _ = Location.objects.get_or_create(name=location)
                user.locations.add(loc_obj)

            user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username': {'read_only': True},
            'password': {'required': False, 'write_only': True}
        }

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.get('locations', [])
        self._password_init = self.initial_data.get('password', None)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        if self._password_init:
            user.set_password(self._password_init)
            user.save()
        if self._locations:
            for location in self._locations:
                loc_obj, _ = Location.objects.get_or_create(name=location)
                user.locations.add(loc_obj)

            user.save()

        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class UserAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
