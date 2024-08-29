from django.contrib import admin
from .models.customer import Customer
from .models.booking import Booking
from .models.tour import Tour

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name','phone','email']
    search_fields = ['id', 'first_name', 'last_name','phone','email']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'state', 'customer', 'tour']
    search_fields = ['id', 'date', 'state', 'customer', 'tour']

class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

