from django.db.models.signals import post_migrate
from django.dispatch import receiver
from Accounts.models import TypeCarteBancaire


@receiver(post_migrate)
def create_initial_type_carte_bancaire(sender, **kwargs):
    if sender.name == 'Accounts':
        TypeCarteBancaire.objects.get_or_create(name="VISA")
        TypeCarteBancaire.objects.get_or_create(name="MasterCard")
        TypeCarteBancaire.objects.get_or_create(name="American Express")
        TypeCarteBancaire.objects.get_or_create(name="Discover")
        TypeCarteBancaire.objects.get_or_create(name="Diners Club")
        TypeCarteBancaire.objects.get_or_create(name="JCB")
