# Generated by Django 5.1 on 2024-08-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Cancelled')], default=0, verbose_name='state'),
        ),
    ]
