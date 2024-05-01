from django.urls import path
from .views import Vendor_Profile,Vendor_Profile_Specific

urlpatterns = [
    path('vendors/',Vendor_Profile.as_view(),name='Vendor-register-list'),
    path('vendors/<int:pk>',Vendor_Profile_Specific.as_view(),name='Vendor-details'),
    # path('api/', include("Vendor.urls")),
]
