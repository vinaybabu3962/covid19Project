from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from coronaRapidTest import views

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='coronaRapidTest'),
    path('count', views.count, name='count'),
    ]
    
    