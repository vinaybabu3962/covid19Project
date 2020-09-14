from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from coronaTs import views

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='coronaTs'),
    path('count', views.count, name='count'),
    path('count1', views.dis, name='count1'),
    
    
]
