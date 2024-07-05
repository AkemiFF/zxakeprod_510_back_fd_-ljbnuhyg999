from rest_framework.permissions import BasePermission


class IsClientUser(BasePermission):
    """
    Permission qui permet uniquement aux utilisateurs du modèle Client d'accéder à la vue.
    """

    def has_permission(self, request, view):
        return bool(request.user)


class IsResponsableHotel(BasePermission):
    """
    Permet l'accès uniquement aux utilisateurs qui sont responsables d'un type 'Hotel'.
    """

    def has_permission(self, request, view):
        # Vérifiez que l'utilisateur est authentifié
        if not request.user or not request.user.is_authenticated:
            return False

        # Vérifiez que l'utilisateur est un ResponsableEtablissement et que son type_responsable est 'Hotel'
        return hasattr(request.user, 'type_responsable') and request.user.type_responsable.type_name == 'Hotel'
