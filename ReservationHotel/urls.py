from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    
    # Creation responsable etablissement
    path('responsable/', include('ResponsableEtablissement.urls')),
    path('responsable/', include('Hebergement.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
    path('api/', include('API.urls')),
]
>>>>>>> origin/Mirado
