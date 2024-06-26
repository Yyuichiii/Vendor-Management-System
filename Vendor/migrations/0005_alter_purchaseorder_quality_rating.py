# Generated by Django 5.0.4 on 2024-05-05 06:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0004_historicalperformance_purchaseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(blank=True, default=None, help_text='Rating given to the vendor for this purchase order (nullable, range: 0 to 5).', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
