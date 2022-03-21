from django.contrib import admin
from django.urls import path
from Event import views

urlpatterns = [
    path('', views.index, name="home")
]