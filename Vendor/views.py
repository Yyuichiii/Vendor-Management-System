from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import VendorProfileSerializers
from .models import Vendor_Model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import AccessToken


class Vendor_Profile(APIView):

    def post(self, request, format=None):
        """
        Handles Vendor registration requests.

        Returns:
        - Success message and token on successful registration.
        - Error messages on invalid data.
        """
        serializer = VendorProfileSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = str(AccessToken.for_user(user))
            return Response({'msg': 'Registration Success', 'token': token}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format=None):
        
        user=Vendor_Model.objects.all()
        serializer = VendorProfileSerializers(user,many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)



class Vendor_Profile_Specific(APIView):

    def get(self, request, pk, format=None):
        # Retrieve the vendor instance or raise a 404 error if not found
        vendor = get_object_or_404(Vendor_Model, pk=pk)
        
        # Serialize the vendor instance
        serializer = VendorProfileSerializers(vendor)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def put(self, request, pk, format=None):
        # Retrieve the vendor instance or raise a 404 error if not found
        vendor = get_object_or_404(Vendor_Model, pk=pk)
        # Serialize the vendor instance
        serializer = VendorProfileSerializers(instance=vendor,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        vendor = get_object_or_404(Vendor_Model, pk=pk)

        vendor.delete()

        return Response({"success":"The Vendor has been deleted"},status=status.HTTP_200_OK)

