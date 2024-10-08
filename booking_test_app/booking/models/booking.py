from django.db import models
from .customer import Customer
from .tour import Tour
import datetime

class Booking(models.Model):
    date = models.DateField (default=datetime.datetime.today)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True)

    class State(models.IntegerChoices):
        Pending = 0, 'Active'
        Approved = 1, 'Cancelled'

    state = models.IntegerField(choices=State.choices,verbose_name=('state'), default= 0)