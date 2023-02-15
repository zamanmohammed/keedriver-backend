# Generated by Django 4.1.6 on 2023-02-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TripDeatil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TripType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=255)),
                ('pickup_time', models.DateTimeField()),
                ('drop_location', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer1', to='accounts.customer')),
                ('trip_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trips.triptype')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=255)),
                ('pickup_time', models.DateTimeField()),
                ('drop_location', models.CharField(blank=True, max_length=255, null=True)),
                ('drop_time', models.DateTimeField()),
                ('landmark', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('amount_status', models.CharField(choices=[('NOT PAID', 'Not Paid'), ('PAID', 'Paid')], default='NOT PAID', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to='accounts.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='driver', to='accounts.driver')),
                ('trip_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trips.triptype')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('NOT PAID', 'Not Paid'), ('PAID', 'Paid')], default='NOT PAID', max_length=150)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip1')),
            ],
        ),
        migrations.CreateModel(
            name='AssignDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='driver1', to='accounts.driver')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip1')),
            ],
        ),
    ]
