from django.shortcuts import render
from django.http import HttpResponse

taxrate=0.15

def index(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def calculate(request, amount):
    total=float(amount)*(1+taxrate)
    return HttpResponse(f"<h1>Total after calculate tax is {total:.3f}</h1>")

def showtax(request):
    return HttpResponse(f"<h1>The tax rate is {taxrate * 100}%</h1>")




# Create your views here.