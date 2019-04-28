from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView

from map.forms import CarForm

class HomePageView(TemplateView):
	template_name = 'map/homepage.html'

	def get_context_data(self, *args, **kwargs):
		print("get_context_data")
		numberplate = self.request.GET.get("number_plate")	# Remove later
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate)
		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context


	def post(self, request):
		if request.method == "POST":
			number_plate = request.POST['car']
			set_car = Car.objects.get(number_plate=number_plate)
			set_car.available = True
			set_car.save()
		return render(request, self.template_name)

class ConfirmationPage(TemplateView):
	template_name = 'confirmation/confirmation.html'

	# Recieving get request from form
	def get(self, request, number_plate):
		set_car = Car.objects.get(number_plate=number_plate) # Set car object using the number_plate
		#set_car.available = False	# Set the selected car to false so other users can't select the car
		#set_car.save() # Save car object to database
		args = {
        	"car": set_car
    	}
		return render(request, self.template_name, args)
