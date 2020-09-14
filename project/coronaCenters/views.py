
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from corona.models import coronaCenter
from django.views import generic
class IndexView(generic.ListView):
    def get(self,request):
        return render(request,'coronaCenters/five.html')
# Create your views here.
def count(request):
    try:
        type1=request.GET['district']
        type1=type1.lower()
        #print(type1)
        q=coronaCenter.objects.get(district=type1)
        #print(q.centers)
        ctx={}
        ctx['district']=type1
        ctx['list']=((q.centers).split('@'))
        #print((q.centers).split('@'))
    
    
        return render(request,'coronaCenters/five.html',ctx)
    except:
        
        return render(request, 'coronaCenters/five.html', {
               'error_message': "enter district spelling correctly!"
        })
