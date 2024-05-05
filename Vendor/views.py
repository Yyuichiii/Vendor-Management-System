from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import VendorProfileSerializers,PurchaseOrderSerializer,VendorPerformaceSerializer
from .models import Vendor_Model,PurchaseOrder,HistoricalPerformance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

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
            return Response({'msg': 'Registration Success'}, status=status.HTTP_201_CREATED)
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


class Purchase_Order(APIView):

    def post(self, request, format=None):
        serializer=PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        serializer=PurchaseOrderSerializer(PurchaseOrder.objects.all(),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class Purchase_Order_Specific(APIView):

    def get(self, request,pk, format=None):

        PO = get_object_or_404(PurchaseOrder, pk=pk)
        
        serializer = PurchaseOrderSerializer(PO)

        
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def put(self, request, pk, format=None):
        # Retrieve the vendor instance or raise a 404 error if not found
        PO = get_object_or_404(PurchaseOrder, pk=pk)
        # Serialize the vendor instance
        serializer = PurchaseOrderSerializer(instance=PO,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        PO = get_object_or_404(PurchaseOrder, pk=pk)

        PO.delete()

        return Response({"success":"The Order has been deleted"},status=status.HTTP_200_OK)

        
class Purchase_Order_Acknowledge(APIView):
    
    def post(self, request, pk, format=None):
        # Retrieve the PurchaseOrder instance using the provided pk
        PO = get_object_or_404(PurchaseOrder, pk=pk)

        if PO.acknowledgment_date:
            return Response({"Order has been already acknowlegded before"},status=status.HTTP_403_FORBIDDEN)
    
        # Update the acknowledgment_date field to the current date and time
        PO.acknowledgment_date = timezone.now()
        PO.save()

        calculate_response_time(vendor=PO.vendor)
        
    
        # Serialize the PurchaseOrder object
        serializer = PurchaseOrderSerializer(PO)
    
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

def calculate_response_time(vendor):
    vendor_orders = PurchaseOrder.objects.filter(vendor=vendor)
    cumulative_response_time = timedelta()  # Initialize as a timedelta object with zero duration
    n = 0  # Counter for orders with acknowledgment_date

    # Calculate the cumulative response time and count the number of valid orders
    for order in vendor_orders:
        if order.acknowledgment_date and order.issue_date:
            n += 1
            cumulative_response_time += (order.acknowledgment_date - order.issue_date)

    # Calculate the average response time (as a timedelta object) if there are valid orders
    if n > 0:
        average_response_time = cumulative_response_time / n
        
        # Convert average response time to seconds for storage in a numerical field
        average_response_time_seconds = average_response_time.total_seconds()

        # Save the average response time (in seconds) to the vendor
        vendor.average_response_time = average_response_time_seconds
        vendor.save()

class Purchase_Order_Completed(APIView):
    def post(self, request, pk, format=None):
        # Retrieve the PurchaseOrder instance using the provided pk
        PO = get_object_or_404(PurchaseOrder, pk=pk)

        if not PO.acknowledgment_date:
            return Response({"Acknowlegded the order first"},status=status.HTTP_403_FORBIDDEN)

        if PO.status == "completed":
            return Response({"Order has been already completed"},status=status.HTTP_403_FORBIDDEN)


        # Update the status field to 'completed'
        PO.status = 'completed'

        if PO.delivery_date >= timezone.now():
            PO.on_time_delivery=True

        rating=request.data.get('rating')
        if rating:
            PO.quality_rating=rating
        PO.save()

        calculate_vendor_performance(vendor=PO.vendor)

        # Serialize the PurchaseOrder object
        serializer = PurchaseOrderSerializer(PO)
    
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    

def calculate_vendor_performance(vendor):
    vendor_orders = PurchaseOrder.objects.filter(vendor=vendor)
    cumulative_quality_rating=0
    n = 0 
    n2=0 
    n3=0
    for order in vendor_orders:
        if order.quality_rating:
            n += 1
            cumulative_quality_rating += order.quality_rating

        if order.status =="completed":
            n2 +=1

        if order.on_time_delivery == True:
            n3 +=1
            

        
            
    on_time_delivery= n3 / vendor_orders.count()
    average_quality_rating=cumulative_quality_rating / n
    fulfillment_rate = n2 / vendor_orders.count()

    vendor.quality_rating_avg = average_quality_rating
    vendor.fulfillment_rate = fulfillment_rate
    vendor.on_time_delivery_rate=on_time_delivery
    vendor.save()
    store_performace_data_HistoricalPerformance(vendor)



class Vendor_Performance(APIView):
    def get(self, request, pk, format=None):
        vendor = get_object_or_404(Vendor_Model, pk=pk)

        serializer=VendorPerformaceSerializer(vendor)

        return Response(serializer.data, status=status.HTTP_200_OK)
    


def store_performace_data_HistoricalPerformance(vendor):
    data=HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )

    data.save()


        