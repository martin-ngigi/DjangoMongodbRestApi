from django.urls import path
from accounts import views

urlpatterns = [
    path('myuser/', views.user_list),
    path('myuser/<int:id>/', views.user_details),
]