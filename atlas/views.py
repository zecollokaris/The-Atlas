from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path

def index(request):
    return render(request, 'display/home.html')