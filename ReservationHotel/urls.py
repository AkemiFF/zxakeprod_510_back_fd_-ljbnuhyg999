from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Creation responsable etablissement
    path('responsable/', include('ResponsableEtablissement.urls')),
    path('', include('Hebergement.urls'))
]
