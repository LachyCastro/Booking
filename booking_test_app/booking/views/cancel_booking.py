from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models.booking import Booking
from django.shortcuts import get_object_or_404

class CancelBooking(APIView):
    def post(self, request, pk):
        booking = get_object_or_404(Booking, id=pk)
        booking.state = Booking.State.Denied
        booking.save()
        return Response(status=status.HTTP_204_NO_CONTENT)