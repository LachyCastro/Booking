from rest_framework.generics import CreateAPIView
from booking.models.booking import Booking
from booking.serializers.booking import BookingSerializer

class BookingCreate(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
