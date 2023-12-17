from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.


posts = [
    {
        "slug": "travel-on-the-world",
        "author": "Danny Duong",
        "title": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti",
        "image": "post-1.jpg",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti,Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
        """,
        "date": date(2020, 7, 20)
    },
    {
        "slug": "hiking-the-mountain",
        "author": "Danny Duong",
        "title": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti",
        "image": "post-2.jpg",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti,Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
        """,
        "date": date(2022, 5, 12)
    },
    {
        "slug": "explore-vietnam",
        "author": "Danny Duong",
        "title": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti",
        "image": "post-3.jpg",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti,Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
        """,
        "date": date(2021, 12, 4)
    },
]


def blog_page(request):
    return render(request, "index.html")


def posts_page(request):
    return HttpResponse("ALl Posts Page")


def post_detail(request, slug):
    # detailed_post = posts[slug]
    # return render(request, "post-detail.html", {
    #     "post": detailed_post
    # })
    pass
