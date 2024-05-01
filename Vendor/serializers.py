from rest_framework import serializers,pagination
from .models import Vendor_Model

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
        fields = ['vendor_code', 'name', 'password', 'password2', 'contact_details','address']
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
        print("as")

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
    


