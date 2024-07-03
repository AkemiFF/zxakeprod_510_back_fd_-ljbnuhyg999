from django.urls import path
from Hebergement import views

urlpatterns = [
    path('api/images-chambre/', views.ImageChambreListAPIView.as_view(),
         name='images-chambre-list'),
]
