"""
URL configuration for booking_test_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking.swagger import schema_view
from booking.views.list_booking import  *
from booking.views.cancel_booking import *
from booking.views.create_booking import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/bookings/', BookingList.as_view(), name='booking-list-api'),
    path('api/bookings/<int:pk>/cancel/', CancelBooking.as_view(), name='booking-cancel-api'),
    path('api/bookings/new/', BookingCreate.as_view(), name='booking-create-api'),
]
