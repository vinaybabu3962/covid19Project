from django.shortcuts import render
# q=(coronaDist.objects.all().filter(district='nalgonda'))[:5:-1]
import matplotlib
import numpy as np
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#q=(coronaDist.objects.all().filter(district='nalgonda'))[::-1]
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from corona.models import coronaDist
from django.views import generic
class IndexView(generic.ListView):
    def get(self,request):
        return render(request,'coronaDistrict/two.html')
# Create your views here.
def dis(request):
    return render(request,'coronaDistrict/two1.html')
def count(request):
    try:
        date1=request.GET['date']
        district1=request.GET['district']
    
        q=coronaDist.objects.get(date=date1,district=district1)
        ctx={}
        ctx['date']=date1
        ctx['district']=district1
        ctx['positivecases']=q.positiveCases
    
        return render(request,'coronaDistrict/two1.html',ctx)
    except:
        return render(request, 'coronaDistrict/two1.html', {
               'error_message': "enter any date above september 7 and also make sure you enter correct district spelling(give ghmc for hyderabad)!",
        })
def detail(request,id):
    
        
        k={1:'adilabad',2:'komarambheem asifabad',3:'nirmal',4:'mancherial',5:'nizamabad',6:'jagityal',7:'rajanna sircilla',8:'peddapalli',9:'jayashankar bhupalpally',10:'kamareddy',11:'karimnagar' ,12:'sangareddy',13:'medak',14:'siddipet',15:'warangal urban',16:'warangal rural',17:'mulugu',18:'bhadradri kothagudem',19:'mahabubabad',20:'jangoan',21:'yadadri bhongir',22:'medchal malkajigiri',23:'vikarabad',24:'ghmc',25:'rangareddy',26:'narayanapet',27:'mahabubnagar',28:'jogulamba gadwal',29:'wanaparthy',30:'nalgonda',31:'suryapet',32:'khammam',33:'nagarkurnool'}
        district1=k[id]
        q=(coronaDist.objects.all().filter(district=district1))[::-1]
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
        
        out=df.plot.line(title="Comparison of covid cases in past 5 days in " +k[id] )
        out.set_xlabel("Dates")
        out.set_ylabel("Positive cases")
        
        plt.savefig('coronaDistrict/static/out')
        ctx={}
        ctx['date']='2020-09-09'
        ctx['district']=k[id]
        
        
        
       
        return render(request,'coronaDistrict/two.html',ctx)
    
