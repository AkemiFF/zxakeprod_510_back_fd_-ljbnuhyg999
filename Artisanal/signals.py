from django.db.models.signals import post_migrate
from django.dispatch import receiver
from Artisanal.models import TypeResponsable


@receiver(post_migrate)
def create_initial_type_responsable(sender, **kwargs):
    if sender.name == 'Artisanal':  # Remplacez 'Artisanal' par le nom de votre application Django
        TypeResponsable.objects.get_or_create(type_name="Hotel")
        TypeResponsable.objects.get_or_create(type_name="Artisanal")
        TypeResponsable.objects.get_or_create(type_name="Tour Operateur")
