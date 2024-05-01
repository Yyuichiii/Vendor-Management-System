from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vendor_Model

class VendorAdmin(UserAdmin):
    list_display = ('vendor_code', 'name', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('vendor_code', 'name', 'contact_details', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
        ('Performance', {'fields': ('on_time_delivery_rate', 'quality_rating_avg','average_response_time','fulfillment_rate')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('vendor_code', 'name', 'contact_details', 'address', 'password1', 'password2', 'is_active', 'is_admin')}
        ),
    )
    search_fields = ('vendor_code', 'name')
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(Vendor_Model, VendorAdmin)
