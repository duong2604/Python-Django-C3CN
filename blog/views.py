from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog_page(request):
    return render(request, "index.html")


def posts_page(request):
    return HttpResponse("ALl Posts Page")


def post_detail(request, slug):
    return HttpResponse(f"Detailed Post Page with slug {slug}")
