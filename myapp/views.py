from django.shortcuts import render
from django.http import HttpResponse
#from .forms import RegistrationForm
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
#import requests
#import json
from myapp.forms import LoginForm
from myapp.models import Crop_details

#heroku git:remote -a cropdata
def home(request):
	context = {'list': "list"}
	return render(request, 'index.html', context)


def cotton(request):
	context = {'list': "list"}
	form = LoginForm() 
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			Name = request.POST.get('Name', '')
			Phone = request.POST.get('Phone', '')
			FieldLocation = request.POST.get('FieldLocation', '')
			CropAcres = request.POST.get('CropAcres', '')
			Crop_details_obj = Crop_details(Name=Name,Phone=Phone,FieldLocation=FieldLocation,CropAcres=CropAcres)
			Crop_details_obj.save()

			return HttpResponseRedirect('/')

		else:
			return HttpResponseRedirect('index.html')
			#form = LoginForm()

	return render(request, 'cotton.html', { 'form': form ,})

	#return render(request, 'cotton.html', context)

def contact(request):
	context = {'list': "list"}
	return render(request, 'contact.html', context)

def about(request):
	context = {'list': "list"}
	return render(request, 'aboutus.html', context)


def registration(request):
	form = RegistrationForm()
	context = { "myregistrationform":form }
	return render(request, 'registration.html',context)


