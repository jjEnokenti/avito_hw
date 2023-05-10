from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from selection.custom_permissions import IsOwnerOrStaff
from selection.models import Selection
from selection.serializers import (
    ListSelectionSerializer,
    CreateSelectionSerializer,
    RetrieveSelectionSerializer,
    UpdateSelectionSerializer,
    DestroySelectionSerializer
)


class ListSelectionView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = ListSelectionSerializer
    # permission_classes = [IsAuthenticated]


class RetrieveSelectionView(generics.RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = RetrieveSelectionSerializer
    permission_classes = [IsAuthenticated]


class CreateSelectionView(generics.CreateAPIView):
    queryset = Selection
    serializer_class = CreateSelectionSerializer
    permission_classes = [IsAuthenticated]


class UpdateSelectionView(generics.UpdateAPIView):
    queryset = Selection
    serializer_class = UpdateSelectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class DestroySelectionView(generics.DestroyAPIView):
    queryset = Selection
    serializer_class = DestroySelectionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]
