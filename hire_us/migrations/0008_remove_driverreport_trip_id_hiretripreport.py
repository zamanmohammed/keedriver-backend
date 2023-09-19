# Generated by Django 4.2.4 on 2023-09-11 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_driverprofile_license_expiry_date_and_more'),
        ('hire_us', '0007_driverreport_trip_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverreport',
            name='trip_id',
        ),
        migrations.CreateModel(
            name='HireTripReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.driver')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire_us.hireusreport')),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hire_us.hiretrips')),
            ],
        ),
    ]
