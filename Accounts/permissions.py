from rest_framework.permissions import BasePermission


class IsClientUser(BasePermission):
    """
    Permission qui permet uniquement aux utilisateurs du modèle Client d'accéder à la vue.
    """

    def has_permission(self, request, view):
        return bool(request.user)
