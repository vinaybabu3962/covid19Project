from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from coronaDistrict import views

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='coronaDistrict'),
    path('count', views.count, name='count'),
    path('dis', views.dis, name='coronaDistrict1'),
    path('<int:id>/', views.detail, name='detail'),
    
    
]