from django.urls import path
from .views import Vendor_Profile,Vendor_Profile_Specific,Purchase_Order,Purchase_Order_Specific,Purchase_Order_Acknowledge,Purchase_Order_Completed,Vendor_Performance

urlpatterns = [
    path('vendors/',Vendor_Profile.as_view(),name='Vendor-register-list'),
    path('vendors/<int:pk>',Vendor_Profile_Specific.as_view(),name='Vendor-details'),
    path('vendors/<int:pk>/performance',Vendor_Performance.as_view(),name='Vendor-Performance'),
    path('purchase_orders/',Purchase_Order.as_view(),name='Purchase-order'),
    path('purchase_orders/<int:pk>',Purchase_Order_Specific.as_view(),name='Purchase-order-details'),
    path('purchase_orders/<int:pk>/acknowledge',Purchase_Order_Acknowledge.as_view(),name='Purchase-order-acknowledge'),
    path('purchase_orders/<int:pk>/completed',Purchase_Order_Completed.as_view(),name='Purchase-order-completed'),
    # path('api/', include("Vendor.urls")),
]
