from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
challanges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk everyday at least 20 minute every day!",
    "march": "Learn Django for at least 20 minutes every day!"
}
def january(request):
    return HttpResponse('Eat no meat for the entire month!')

def february(request):
    return HttpResponse('Walk everyday at least 20 minute every day!')

def monthly_challenge(request, month):
    try:
        challenge = challanges[month]
    except:
        return HttpResponseNotFound("Month not supported!")
    
    return HttpResponse(challenge)