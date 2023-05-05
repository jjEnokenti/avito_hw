from rest_framework import serializers

from ads.models import Ad
from ads.serializers.ad import AdSelectionSerializer
from selection.models import Selection


class ListSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name')


class RetrieveSelectionSerializer(serializers.ModelSerializer):
    items = AdSelectionSerializer(many=True)

    class Meta:
        model = Selection
        fields = ('id', 'items', 'owner', 'name')


class CreateSelectionSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Selection
        fields = '__all__'
        # extra_kwargs = {
        #     'id': {'required': False}
        # }

    def is_valid(self, *, raise_exception=False):
        self._items = self.initial_data.get('items', [])

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)
        if self._items:
            for item in self._items:
                ad_object = Ad.objects.get(pk=item)
                selection.items.add(ad_object)
            selection.save()

        return selection


class UpdateSelectionSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )
    removes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Selection
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def is_valid(self, *, raise_exception=False):
        self._items = self.initial_data.get('items', [])
        self._removes = self.initial_data.get('removes', [])

        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        selection = super().save()

        if self._items:
            for item in self._items:
                ad_object = Ad.objects.get(pk=item)
                selection.items.add(ad_object)
            selection.save()

        if self._removes:
            for item in self._removes:
                ad = Ad.objects.get(pk=item)
                selection.items.remove(ad)
            selection.save()

        return selection


class DestroySelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('id',)
