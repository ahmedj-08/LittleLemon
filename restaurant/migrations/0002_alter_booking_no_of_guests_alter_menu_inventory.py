# Generated by Django 5.1.7 on 2025-05-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(verbose_name=6),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(verbose_name=5),
        ),
    ]
