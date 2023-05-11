from rest_framework.permissions import BasePermission

from users.models.user import User


class IsOwnerOrStaff(BasePermission):
    message = 'Only owner can to edit or delete a selection'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.role in (User.ADMIN, User.MODERATOR)
