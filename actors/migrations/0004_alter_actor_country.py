# Generated by Django 5.1.5 on 2025-01-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_rename_nationality_actor_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='country',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil'), ('SPAIN', 'Espanha'), ('FRANCE', 'França'), ('MEXICO', 'México'), ('ARGENTINA', 'Argentina')], max_length=100, null=True),
        ),
    ]
