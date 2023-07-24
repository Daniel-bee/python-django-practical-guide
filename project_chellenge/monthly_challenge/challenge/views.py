from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader  import render_to_string
# Create your views here.
challanges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk everyday at least 20 minute every day!",
    "march": "Learn Django for at least 20 minutes every day!"
}
def index(request):
    month_link = ""
    months = list(challanges.keys())
    for month in months:
        dir_ = reverse('monthly-challenge', args=[month])
        month_link += f"<li><a href='{dir_}'>{month.capitalize()}</a></li>"
    path = f"<ul>{month_link}</ul>"
    return HttpResponse(path)
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
        return render(request, "challenge/challenge.html", {"text":challenge, "title": month})
    except:
        return HttpResponseNotFound("Month not supported!")
    