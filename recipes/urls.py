from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('lunch/', views.lunch, name='lunch'),
    path('SoyChicken/', views.SoyChicken, name='SoyChicken'),
]