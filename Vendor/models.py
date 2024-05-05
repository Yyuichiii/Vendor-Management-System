from django.db import models
from .managers import MyVendorManager
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Vendor_Model(AbstractBaseUser):
    """
    Custom Vendor model 
    """
    vendor_code = models.CharField(
        max_length=50,
        unique=True,
        help_text="The unique identifier of the vendor."
    )
    name = models.CharField(max_length=200, help_text="The name of the vendor.")
    contact_details = models.TextField(help_text="Contact details of the vendor.")
    address = models.TextField(help_text="Address of the vendor.")
    on_time_delivery_rate = models.FloatField(default=0.0, help_text="Rate of on-time delivery.")
    quality_rating_avg = models.FloatField(default=0.0, help_text="Average quality rating.")
    average_response_time = models.FloatField(default=0.0, help_text="Average response time in seconds")
    fulfillment_rate = models.FloatField(default=0.0, help_text="Fulfillment rate.")

    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this vendor should be treated as active."
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates whether this vendor has admin access."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the vendor was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the vendor was last updated."
    )

    objects = MyVendorManager()

    USERNAME_FIELD = "vendor_code"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        """
        Return a string representation of the vendor, which is their name.
        """
        return self.name

    def has_perm(self, perm, obj=None):
        """
        Check if the vendor has a specific permission.
        For simplicity, always return True for admin vendors.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Check if the vendor has permissions to view the app specified by `app_label`.
        For simplicity, always return True.
        """
        return True

    @property
    def is_staff(self):
        """
        Check if the vendor is a member of staff (admin).
        """
        return self.is_admin



class PurchaseOrder(models.Model):
    po_number = models.CharField(
        max_length=50, 
        unique=True, 
        null=False, 
        help_text="Unique number identifying the purchase order."
    )
    vendor = models.ForeignKey(
        'Vendor_Model', 
        on_delete=models.CASCADE, 
        null=False,
        help_text="The vendor associated with this purchase order."
    )
    order_date = models.DateTimeField(
        auto_now_add=True,        
        help_text="The date when the order was placed."
    )
    delivery_date = models.DateTimeField(
         
        help_text="Expected or actual delivery date of the order."
    )
    items = models.JSONField(
        null=False, 
        help_text="Details of items ordered in JSON format.")
    
    
    
    quantity = models.IntegerField(
        null=False, 
        blank=False,
         
        help_text="Total quantity of items in the purchase order."
    )
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')],
        default='pending', 
        help_text="Current status of the purchase order."
    )
    quality_rating = models.FloatField(
        null=True, 
        blank=True, 
        default=None, 
        validators=[
            MinValueValidator(0),  # Minimum value of 0
            MaxValueValidator(5)   # Maximum value of 5
        ],
        help_text="Rating given to the vendor for this purchase order (nullable, range: 0 to 5)."
    )
    issue_date = models.DateTimeField( 
        auto_now_add=True,
        null=True,
        help_text="Timestamp when the purchase order was issued to the vendor."
    )
    acknowledgment_date = models.DateTimeField(
        null=True, 
        blank=True, 
        default=None, 
        help_text="Timestamp when the vendor acknowledged the purchase order (nullable)."
    )

    on_time_delivery=models.BooleanField(default=False,null=True,blank=True,
                                         help_text="True when delivery on or before the delivery date"
                                         )

    def __str__(self):
        return f'PO {self.po_number} - {self.vendor}'

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('Vendor_Model', on_delete=models.CASCADE, help_text='Select the vendor for this performance record.')
    date = models.DateTimeField(help_text='Date of the performance record.')
    on_time_delivery_rate = models.FloatField(default=0.0, help_text='Historical record of the on-time delivery rate (0.0 - 1.0).')
    quality_rating_avg = models.FloatField(default=0.0, help_text='Historical record of the quality rating average (0.0 - 5.0).')
    average_response_time = models.FloatField(default=0.0, help_text='Historical record of the average response time in hours.')
    fulfillment_rate = models.FloatField(default=0.0, help_text='Historical record of the fulfillment rate (0.0 - 1.0).')

    def __str__(self):
        return f'{self.vendor} - {self.date.strftime("%Y-%m-%d")}'