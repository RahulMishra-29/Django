from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. 96db8033 is the polls index.")
# Create your views here.
