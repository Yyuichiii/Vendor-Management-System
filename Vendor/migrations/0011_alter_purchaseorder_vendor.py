# Generated by Django 5.0.4 on 2024-05-05 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0010_alter_purchaseorder_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(help_text='The vendor associated with this purchase order.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
