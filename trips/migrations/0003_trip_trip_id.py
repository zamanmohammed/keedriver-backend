# Generated by Django 4.1.6 on 2023-02-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_alter_trip_trip_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(default='KD2023<built-in function id>', editable=False, max_length=250, unique=True),
        ),
    ]
