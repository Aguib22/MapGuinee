# Generated by Django 4.1.1 on 2023-12-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedagogie', '0003_accompagnement_adminscolaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminscolaire',
            name='type_admin',
            field=models.CharField(choices=[('Gestion_ecole', 'Gestion_ecole'), ('dev_ecole', 'dev_ecole')], default='Gestion_ecole', max_length=123),
        ),
    ]
