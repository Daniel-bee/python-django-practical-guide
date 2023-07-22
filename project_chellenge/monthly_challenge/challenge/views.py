from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
challanges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk everyday at least 20 minute every day!",
    "march": "Learn Django for at least 20 minutes every day!"
}
def january(request):
    return HttpResponse('Eat no meat for the entire month!')

def february(request):
    return HttpResponse('Walk everyday at least 20 minute!')

def monthly_challenges_by_number(request, month):
    months = list(challanges.keys())
   
    if month > len(months) or month <= 0:
        return HttpResponseNotFound("Month not supported!")
    redirect = months[month - 1]
    dir_ = reverse('monthly-challenge', args=[redirect])
    return HttpResponseRedirect(dir_)

def monthly_challenge(request, month):
    try:
        challenge = challanges[month]
    except:
        return HttpResponseNotFound("Month not supported!")
    
    return HttpResponse(challenge)