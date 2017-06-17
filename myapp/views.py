from django.shortcuts import render
from django.http import HttpResponse



def home(request):
	context = {'list': "list"}
	return render(request, 'index.html', context)
