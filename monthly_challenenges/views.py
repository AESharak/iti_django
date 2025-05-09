from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

months_challenges = {
    "january": "Run 20 minutes every day",
    "february": "eat 5 fruits every day",
    "march": "do 30 pushups every day",
    "april": "drink 3 liters of water every day",
    "may": "do 30 squats every day",
    "june": "do 30 burpees every day",
    "july": "do 30 jumping jacks every day",
    "august": "do 30 situps every day",
    "september": "do 30 pushups every day",
    "october": "do 30 jumping jacks every day",
    "november": "do 30 squats every day",
    "december": "spend time with family",
}
def index(request):
    return HttpResponse("Hello, World!, You're at the monthly challenges index.")

def month_challenge_by_name(request,month):
    return HttpResponse(f"{months_challenges[month]} in {month}")

def month_challenge_by_number(request,month):
    months = list(months_challenges.keys())
    return HttpResponseRedirect(reverse("month_challenge_by_name",args=[months[month-1]]))
    # return HttpResponse(f"challenge for {month}")



