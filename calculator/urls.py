from django.urls import include, path
from django.contrib import admin
from . import views

# app_name = 'calculator'
urlpatterns = [
    path('',views.index,name='index'),
    path('submitquery',views.submitquery,name='submitquery'),
]
