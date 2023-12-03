from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

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

    months = list(monthly_challenges.keys())

    return render(request, "index.html", {
        'months': months
    })


def monthly_challenges_by_number(request, month):

    # ['january', 'february',...'december']
    months = list(monthly_challenges.keys())

    monthly_challenge = months[month - 1]

    redirect_path = reverse('monthly', args=[monthly_challenge])

    # http://localhost:8000/challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges_by_string(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges.html", {
            "challenge_text": challenge_text
        })
    except:
        # return HttpResponseNotFound('404 not found!')
        raise Http404('404.html')
