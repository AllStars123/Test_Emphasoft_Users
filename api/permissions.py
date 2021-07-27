from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrUser(BasePermission):
    def has_permission(self, request, view):
        user = view.get_object()
        if user == request.user and request.method in ['PATCH', 'PUT']:
            return True
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
