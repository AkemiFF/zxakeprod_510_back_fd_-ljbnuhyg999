from django.db.models.signals import post_migrate
from django.dispatch import receiver
import Accounts
from Accounts.models import TypeCarteBancaire, TypeResponsable


@receiver(post_migrate)
def create_initial_types(sender, **kwargs):

    TypeResponsable.objects.get_or_create(type_name="Hotel")
    TypeResponsable.objects.get_or_create(type_name="Artisanal")
    TypeResponsable.objects.get_or_create(type_name="Tour Operateur")

    TypeCarteBancaire.objects.get_or_create(name="VISA")
    TypeCarteBancaire.objects.get_or_create(name="MasterCard")
    TypeCarteBancaire.objects.get_or_create(name="American Express")
    TypeCarteBancaire.objects.get_or_create(name="Discover")
    TypeCarteBancaire.objects.get_or_create(name="JCB")
