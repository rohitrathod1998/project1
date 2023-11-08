from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sender(request):
    return HttpResponse('<marquee><h1>response from views </h1></marquee>')