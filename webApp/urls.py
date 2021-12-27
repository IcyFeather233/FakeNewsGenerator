from django.urls import path

from webApp import views

urlpatterns = [
    path('generate', views.generate),
]