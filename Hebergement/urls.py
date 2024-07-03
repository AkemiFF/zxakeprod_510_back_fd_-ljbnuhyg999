from django.urls import path
from .views import *

urlpatterns = [
    path('admin_hebergement', all_hebergements_view, name="liste_hebergement"),
    # path('create_hebergement', create_hebergement, name="creer_hebergement"),
]
