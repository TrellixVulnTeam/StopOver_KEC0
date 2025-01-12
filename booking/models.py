from django.db import models
from django.conf import settings

# Our Booking Model
class Booking(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	start_date = models.DateField(auto_now_add=True)
	start_time = models.TimeField(auto_now_add=True)
	end_date = models.DateField(null=True)
	end_time = models.TimeField(null=True)

	# Customer id for payment
	customer_id = models.CharField(max_length=250)

	# Static car details for the booking
	brand = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	number_plate = models.CharField(max_length=7)
	price = models.IntegerField()
	actual_price = models.IntegerField(default=0)
	start_longitude = models.FloatField(default=None)
	start_latitude = models.FloatField(default=None)
	end_longitude = models.FloatField(default=None, null=True)
	end_latitude = models.FloatField(default=None, null=True)
