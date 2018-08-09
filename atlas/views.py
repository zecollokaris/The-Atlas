from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'display/home.html')