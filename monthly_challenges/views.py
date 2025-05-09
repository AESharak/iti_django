from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    months = list(months_challenges.keys())
    return render(request,"monthly_challenges/all.html",context={
        "all_months": months
    })

def month_challenge_by_name(request,month):
    # return HttpResponse(f"{months_challenges[month]} in {month}")
    return render(request,"monthly_challenges/index.html",{
        "text": months_challenges[month],
        "month": month
    })


def month_challenge_by_number(request,month):
    months = list(months_challenges.keys())
    url = reverse("month_challenge_by_name",args=[months[month-1]])
    return HttpResponseRedirect(url)

def monthly_challenge(request):
#    data = render_to_string("monthly_challenges/index.html")
#    return HttpResponse(data)
    return render(request,"monthly_challenges/index.html",context={
        "text": "Hello",
        "number": 10
    })
