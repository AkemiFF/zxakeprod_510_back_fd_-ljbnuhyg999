from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hebergement', include('Hebergement.urls')),
    path('accounts', include('Accounts.urls'))

]
