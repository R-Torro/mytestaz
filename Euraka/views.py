from django.shortcuts import render
from django.http import HttpResponse

def index (request) :
    return HttpResponse("This was less of a struggle")

# Create your views here.
