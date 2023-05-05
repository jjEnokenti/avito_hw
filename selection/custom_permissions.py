from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Only owner can to edit or delete a selection'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
