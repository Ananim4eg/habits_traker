from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешает доступ только к своим объектам"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
