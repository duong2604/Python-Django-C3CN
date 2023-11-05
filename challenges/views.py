from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

monthly_challenges = {
    "january": "Learn to Python at least 20 minutes everyday.",
    "february": "Eat no meat the entire month!",
    "march": "Do homework very much!",
    "april": "Eat no meat the entire month!",
    "may": "Eat no meat the entire month!",
    "june": "Do homework very much!",
    "july": "Eat no meat the entire month!!",
    "august": "Eat no meat the entire month!",
    "september": "Eat no meat the entire month!",
    "october": "Learn to Python at least 20 minutes everyday.",
    "november": "Eat no meat the entire month!",
    "december": "Do homework very much!",
}


def index(request):
    return HttpResponse("Hello, world!")

# def january(request):
#     return HttpResponse("January: Eat no meat in entire month!")


# def february(request):
#     return HttpResponse("february: Eat no meat in entire month!")

# def march(request):
#     return HttpResponse("March: Eat no meat in entire month!")

def monthly_challenges_by_string(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('404 not found!')
