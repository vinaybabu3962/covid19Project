from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from corona.models import coronaLab
from django.views import generic
class IndexView(generic.ListView):
    def get(self,request):
        return render(request,'coronaLabs/three.html')
# Create your views here.
def count(request):
    try:
        type1=request.GET['type']
        #print(type1)
        q=coronaLab.objects.get(type=type1)
        #print(q.centers)
        ctx={}
        ctx['type']=type1
        ctx['list']=((q.centers).split('@'))
        #print((q.centers).split('@'))
    
    
        return render(request,'coronaLabs/three.html',ctx)
    except:
        return render(request, 'coronaRapidTest/four.html', {
               'error_message': "enter  spelling correctly (give only government /private)!"
        })