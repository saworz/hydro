# Generated by Django 4.2.11 on 2024-03-31 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_measurement_measured_at_alter_measurement_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measured_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
