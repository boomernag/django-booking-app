from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking'),
    path('make_a_booking/', views.make_a_booking, name='make_a_booking'),
    path('book/', views.book, name='book'),
]