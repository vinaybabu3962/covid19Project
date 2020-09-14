from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import generic
class IndexView(generic.ListView):
    def get(self,request):
        return render(request,'corona/page.html')