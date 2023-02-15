# Generated by Django 4.1.6 on 2023-02-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('COMPELETED', 'Compeleted'), ('CANCELLED', 'Cancelled')], default='ACTIVE', max_length=25),
        ),
    ]
