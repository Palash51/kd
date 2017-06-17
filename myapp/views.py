from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
	context = {'list': "list"}
	return render(request, 'index.html', context)
