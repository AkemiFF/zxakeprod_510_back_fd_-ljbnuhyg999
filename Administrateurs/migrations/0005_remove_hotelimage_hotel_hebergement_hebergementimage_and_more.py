# Generated by Django 5.0.6 on 2024-07-03 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrateurs', '0004_rename_image_hotel_hotelimage_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelimage',
            name='hotel',
        ),
        migrations.CreateModel(
            name='Hebergement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_hebergement', models.CharField(max_length=100)),
                ('description_hebergement', models.TextField()),
                ('adresse_hebergement', models.CharField(max_length=200)),
                ('ville_hebergement', models.CharField(max_length=100)),
                ('nombre_etoile_hebergement', models.IntegerField()),
                ('latitude_hebergement', models.FloatField()),
                ('longitude_hebergement', models.FloatField()),
                ('image_hebergement', models.ImageField(blank=True, null=True, upload_to='hebergement_images')),
                ('type_hebergement', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('responsable_hebergement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hebergements', to='Administrateurs.responsable_etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='HebergementImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='hebergement_images')),
                ('legende_hebergement', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hebergement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Administrateurs.hebergement')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='HotelImage',
        ),
    ]
