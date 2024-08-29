from rest_framework.generics import ListAPIView
from booking.models.booking import Booking
from booking.serializers.booking import BookingSerializer

class BookingList(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
