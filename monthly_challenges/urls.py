from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('challenges-view', views.monthly_challenge, name="monthly_challenge"),
    path('<int:month>', views.month_challenge_by_number, name="month_challenge_by_number"),
    path('<str:month>', views.month_challenge_by_name, name="month_challenge_by_name"),
]