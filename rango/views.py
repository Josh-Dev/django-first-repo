from django.shortcuts import render

# Create your views here.

# import HttpResponse from the django module
from django.http import HttpResponse

# each view exists as a function
# takes an HttpRequest as an argument, which contains request info
# Returns a RESPONSE
def index(request):
    return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page! <a href='/rango/'>Home</a>");



