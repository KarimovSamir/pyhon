# Generated by Django 4.0.8 on 2023-10-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPSTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_id', models.CharField(max_length=50, unique=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]