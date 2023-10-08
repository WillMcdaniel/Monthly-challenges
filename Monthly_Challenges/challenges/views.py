from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "This is the January challenge",
    "february": "This is the February challenge",
    "march": "This is the March challenge",
    "april": "This is the April challenge",
    "may": "This is the May challenge",
    "june": "This is the June challenge",
    "july": "This is the July challenge",
    "august": "This is the August challenge",
    "september": "This is the September challenge",
    "october": "This is the October challenge",
    "november": "This is the November challenge",
    "december": "This is the December challenge"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month not found")
