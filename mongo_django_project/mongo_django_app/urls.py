from django.urls import path
from mongo_django_app import views

urlpatterns = [
    path('drinks/', views.drink_list),
]