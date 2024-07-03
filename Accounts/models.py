from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class TypeResponsable(models.Model):
    type_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True,
    )

    def __str__(self):
        return self.type_name


class ResponsableEtablissement(models.Model):
    email_responsable = models.EmailField()
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)

    password_responsable = models.CharField(max_length=100)

    numero_responsable = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^(032|033|034|038)\d{7}$', message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_responsable = models.ForeignKey(
        TypeResponsable, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom_responsable} {self.prenom_responsable} ({self.type_responsable})"

    def save(self, *args, **kwargs):
        self.password_responsable = make_password(self.password_responsable)
        super().save(*args, **kwargs)


class TypeCarteBancaire(models.Model):
    name = models.CharField(max_length=50, unique=True)
    regex_pattern = models.CharField(
        max_length=255,
        help_text="Expression régulière pour la validation du numéro de carte bancaire",
        default=r'^$'
    )

    def __str__(self):
        return self.name


class Client(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True, blank=True

    )
    email = models.EmailField(_('email address'), unique=True)
    numero_client = models.CharField(max_length=10)
    numero_bancaire_client = models.CharField(max_length=19, null=True, validators=[RegexValidator(
        regex=r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})$',
        message='Le numéro de carte bancaire n\'est pas valide.'
    )])
    type_carte_bancaire = models.ForeignKey(
        TypeCarteBancaire, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')


Client._meta.get_field('password').validators = [
    RegexValidator(
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
        message=_(
            'Le mot de passe doit contenir au moins 8 caractères, une lettre et un chiffre.')
    )
]

ResponsableEtablissement._meta.get_field('password_responsable').validators = [
    RegexValidator(
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
        message=_(
            'Le mot de passe doit contenir au moins 8 caractères, une lettre et un chiffre.')
    )
]
