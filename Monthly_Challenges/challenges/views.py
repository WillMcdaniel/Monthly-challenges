from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

#def january(request):
#    return HttpResponse("This is January")


#def february(request):
#    return HttpResponse("This is February")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    if month == "january":
        challenge_text: str = "This is the January challenge"
    else:
        return HttpResponseNotFound("This is not the month you are looking for")
    return HttpResponse(challenge_text)
