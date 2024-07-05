# Generated by Django 5.0.4 on 2024-07-03 16:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourOperateur', '0003_imagevoyage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation_voyage', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('confirmed', 'Confirmée'), ('pending', 'En attente'), ('cancelled', 'Annulée')], default='pending', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='TourOperateur.voyage')),
            ],
        ),
    ]
