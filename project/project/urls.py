
from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from corona import views

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='home'),
    path('coronaTs/', include('coronaTs.urls')),
    path('coronaDistrict/', include('coronaDistrict.urls')),
    path('coronaLabs/', include('coronaLabs.urls')),
    path('coronaRapidTest/', include('coronaRapidTest.urls')),
    path('coronaCenters/', include('coronaCenters.urls')),
]
