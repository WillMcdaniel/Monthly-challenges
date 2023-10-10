from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,

    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month not found")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return Http404("Month not found")
