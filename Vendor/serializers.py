from rest_framework import serializers
from .models import Vendor_Model,PurchaseOrder,HistoricalPerformance

class VendorProfileSerializers(serializers.ModelSerializer):
    """
    Serializer for Vendor registration.

    Attributes:
        password2 (serializers.CharField): Confirmation password field.
        Code (serializers.CharField): Referral code field.
    """

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        """
        Meta class for model and fields specification.
        """

        model = Vendor_Model
        fields = ['id','vendor_code', 'name', 'password', 'password2', 'contact_details','address']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """
        Validates password match.
        """

        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords don't match")

        return attrs

    def create(self, validated_data):
        """
        Creates a new Vendor instance and rewards referred users with points.
        """
        

        vendor_code = validated_data.get('vendor_code')
        name = validated_data.get('name')
        password = validated_data.get('password')
        
        vendor_code=Vendor_Model.objects.create_user(vendor_code, name,password)

        return vendor_code


    def update(self, instance, validated_data):
        
        instance.vendor_code = validated_data.get('vendor_code', instance.vendor_code)
        instance.name = validated_data.get('name', instance.name)
        instance.contact_details = validated_data.get('contact_details', instance.contact_details)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        return instance
    

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields = ['id','po_number','vendor', 'delivery_date', 'quantity','status','quality_rating','issue_date','acknowledgment_date','on_time_delivery','items']

    def create(self, validated_data):       
        
        po=PurchaseOrder.objects.create(**validated_data)
        po.save()
        return po

    def update(self, instance, validated_data):
        
        instance.po_number = validated_data.get('po_number', instance.po_number)
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.items = validated_data.get('items', instance.items)
        instance.save()

        return instance

class VendorPerformaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_Model
        fields = ['on_time_delivery_rate','quality_rating_avg','average_response_time', 'fulfillment_rate']

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'