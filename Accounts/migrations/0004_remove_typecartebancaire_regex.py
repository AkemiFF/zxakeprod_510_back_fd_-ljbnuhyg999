# Generated by Django 5.0.4 on 2024-07-03 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_rename_mdp_responsable_responsableetablissement_password_responsable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typecartebancaire',
            name='regex',
        ),
    ]
