
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from corona.models import coronaRapid
from django.views import generic
class IndexView(generic.ListView):
    def get(self,request):
        return render(request,'coronaRapidTest/four.html')
# Create your views here.
def count(request):

    try:
        type1=request.GET['district']
        #print(type1)
        q=coronaRapid.objects.get(district=type1)
        #print(q.centers)
        ctx={}
        ctx['district']=type1
        ctx['list']=((q.centers).split('@'))
        #print((q.centers).split('@'))
    
    
        return render(request,'coronaRapidTest/four.html',ctx)
    except:
        return render(request, 'coronaRapidTest/four.html', {
               'error_message': "enter district spelling correctly!"
        })

# Create your views here.
