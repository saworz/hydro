# Generated by Django 4.2.11 on 2024-03-30 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(choices=[('Ph', 'Ph'), ('Temperature', 'Temperature'), ('Tds', 'Tds')], max_length=11)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='systems.hydrosystem')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='sensors.sensor')),
            ],
        ),
    ]
