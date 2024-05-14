from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        # return obj.User == request.user
        # return True
