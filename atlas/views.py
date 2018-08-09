from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path
from . import models
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
'''
The @login_required declarator limits access of view function to only 
authenticated users
'''
#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#



#################################################################################################################################################################################
#INDEX PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Index page view function
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'display/home.html')

#################################################################################################################################################################################
#################################################################################################################################################################################