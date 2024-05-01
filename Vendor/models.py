from django.db import models
from .managers import MyVendorManager
from django.contrib.auth.models import AbstractBaseUser

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
    average_response_time = models.FloatField(default=0.0, help_text="Average response time.")
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
