from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('responsable/', include('ResponsableEtablissement.urls')),
    path('api', include('API.urls'))
]
