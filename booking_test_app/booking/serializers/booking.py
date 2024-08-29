from rest_framework import serializers
from booking.models.booking import Booking
from booking.serializers.tour import TourSerializer 
from booking.serializers.customer import CustomerSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'date', 'customer', 'tour', 'state']
