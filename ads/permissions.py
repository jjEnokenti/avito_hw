from rest_framework.permissions import BasePermission


class CanEditOrDelete(BasePermission):
    message = 'Only owner, admin or moderator can to edit or delete an ad'

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.author
