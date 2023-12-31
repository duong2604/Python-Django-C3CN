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
    {
        "slug": "enjoy-food",
        "author": "Danny Duong",
        "title": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti",
        "image": "post-3.jpg",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti,Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deleniti
        """,
        "date": date(2019, 12, 8)
    },
]


def blog_page(request):

    data = sorted(posts, key=lambda x: x['date'])
    latest_post = data[0:3]
    return render(request, "index.html", {
        "latest_post": latest_post
    })


def posts_page(request):
    return render(request, "all-post.html", {
        "posts": posts
    })


def post_detail(request, slug):

    # Lặp qua tất  các bài post
    # Tìm bài post có slug === slug(truyền vào)
    # Trả ra bai post render vè giao diện

    # post = [post for post in posts if post['slug'] == slug]
    identified_post = next(post for post in posts if post['slug'] == slug)

    return render(request, "post-detail.html", {
        "post": identified_post
    })
