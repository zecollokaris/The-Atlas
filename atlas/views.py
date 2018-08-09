from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'display/home.html')