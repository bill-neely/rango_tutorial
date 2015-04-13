from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world <br> Find out <a href='about'>about</a> us")

def about(request):
	return HttpResponse("This is the about Rango page. <br> Go <a href='/rango'>Home</a>")

