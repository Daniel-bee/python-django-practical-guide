from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def january(request):
    return HttpResponse('Eat no meat for the entire month!')

def february(request):
    return HttpResponse('Walk everyday at least 20 minute every day!')

def monthly_challenge(request, month):
    challenge = None
    if month == "january":
        challenge =  "Eat no meat for the entire month!"
    elif month == "february":
        challenge = "Walk everyday at least 20 minute every day!"
    elif month == "march":
        challenge = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("Month not supported!")
    
    return HttpResponse(challenge)