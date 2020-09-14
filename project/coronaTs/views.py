from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
from corona.models import coronaTelangana
from django.views import generic
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
class IndexView(generic.ListView):
    def get(self,request):
        
        q=(coronaTelangana.objects.all())[::-1]
        print(q)
        a=[]
        b=[]
        l=0
        for i in q:
            if l==5:
                break
            m,n,o=(i.date).split('-')
            a.append(o + "-" + n)
            b.append(int(i.positiveCases))
            l+=1
        print(a,b)
        left = [1, 2, 3, 4, 5]
        
        data={'dates':a,'cases':b}
        df=pd.DataFrame(data)
        df.set_index("dates",drop=True,inplace=True)
        print(df)
        #out=df.plot(kind='bar',x='dates',y='cases',title="Comparison of covid cases in past 5 days in " +k[id] )
        
        out=df.plot.line(title="Comparison of covid cases in telangana in past 5 days" )
        out.set_xlabel("Dates")
        out.set_ylabel("Positive cases")
        
        plt.savefig('coronaTs/static/out1')
        return render(request,'coronaTs/one.html')
# Create your views here.
def dis(request):
        
        return render(request,'coronaTs/one1.html')
def count(request):
    try:
        date1=request.GET['date']
        print(date1)
        q=coronaTelangana.objects.get(date=date1)
        ctx={}
        ctx['date']=date1
        ctx['positivecases']=q.positiveCases
        ctx['negativecases']=q.negativeCases
        ctx['deaths']=q.deaths
        ctx['samplestested']=q.samplesTested
        ctx['homeisolation']=q.homeIsolation
        ctx['casefatalityrate']=q.caseFatalityRate
        ctx['recoveryrate']=q.recoveryRate
        return render(request,'coronaTs/one1.html',ctx)
    except:
        return render(request, 'coronaTs/one1.html', {
               'error_message': "enter any date above september 7",
        })
    
