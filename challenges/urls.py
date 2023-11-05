from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # http://localhost:8000/challenges/january
    path('<month>', views.monthly_challenges_by_string)
]
