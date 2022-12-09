# Generated by Django 4.1.3 on 2022-12-09 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('make', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=16)),
                ('odometer', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('chauffeured', models.BooleanField()),
                ('image', models.CharField(max_length=256)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileageTraveled', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentalNumber', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserveStart', models.DateField()),
                ('reserveNights', models.IntegerField()),
                ('estimateCost', models.IntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneApi.bus')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneApi.guest')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneApi.host')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUp', models.DateField()),
                ('startFuel', models.DecimalField(decimal_places=0, max_digits=2)),
                ('dropOff', models.DateField()),
                ('newOdometer', models.IntegerField()),
                ('endFuel', models.DecimalField(decimal_places=0, max_digits=2)),
                ('totalCost', models.IntegerField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneApi.reservation')),
            ],
        ),
    ]
