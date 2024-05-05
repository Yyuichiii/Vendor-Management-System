# Generated by Django 5.0.4 on 2024-05-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0012_alter_purchaseorder_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='on_time_delivery',
            field=models.BooleanField(blank=True, default=False, help_text='True when delivery on or before the delivery date', null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Timestamp when the purchase order was issued to the vendor.', null=True),
        ),
        migrations.AlterField(
            model_name='vendor_model',
            name='average_response_time',
            field=models.FloatField(default=0.0, help_text='Average response time in seconds'),
        ),
    ]
