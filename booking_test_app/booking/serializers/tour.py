from rest_framework import serializers
from booking.models.tour import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
