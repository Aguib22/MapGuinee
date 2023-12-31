# Generated by Django 4.1.1 on 2023-12-20 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedagogie', '0002_categorie_service_type'),
        ('marketing', '0002_alter_ecolepartenaire_service_delete_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='type_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedagogie.categorie'),
        ),
        migrations.AlterField(
            model_name='livres',
            name='type_livre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedagogie.categorie'),
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]
