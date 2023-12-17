from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_page, name="blog_page"),
    path("posts", views.posts_page, name="posts_page"),
    path("posts/<slug>", views.post_detail, name="post_detail")
]
# http: localhost:8000/
