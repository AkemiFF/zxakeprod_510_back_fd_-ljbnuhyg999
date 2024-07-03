from django.contrib import admin
from Administrateurs.models import *
from BDD.models import *


admin.site.register(Hebergement)
admin.site.register(HebergementImage)
admin.site.register(Accessoire)
admin.site.register(Chambre)
admin.site.register(Reservation)
admin.site.register(Message)
