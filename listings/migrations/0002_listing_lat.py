# Generated by Django 3.2.7 on 2021-10-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=10),
        ),
    ]
