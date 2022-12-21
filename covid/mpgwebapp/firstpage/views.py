from django.shortcuts import render
from django.http import HttpResponse 

#from sklearn.externals import joblib 
#password : j0thsn4@570
import pickle
import pandas as pd
import numpy as np

#reloadModel = pickle.load(open('./models/rf_model.pkl'),"rb",encoding='UTF8')
#22.49 
with open('./models/rollmodel.pkl','rb') as f:
    reloadModel = pickle.load(f) 
# Create your views here.
def index(request):
    context={'a':'HelloWorld'}
    return render(request,'index.html',context)
    #return HttpResponse({'a' :1})

def predictmpg(request):
    print(request)
    if(request.method == 'POST'): 
        temp={}
        temp['GENDER'] = request.POST.get('GENDER')
        temp['AGE'] = request.POST.get('AGE')
        temp['WBC'] = request.POST.get('WBC')
        temp['Platelets'] = request.POST.get('Platelets')
        temp['Neutrophils'] = request.POST.get('Neutrophils')
        temp['Lymphocytes'] = request.POST.get('Lymphocytes') 
        temp['Monocytes'] = request.POST.get('Monocytes') 
        temp['Eosinophils'] = request.POST.get('Eosinophils')
        temp['Basophils'] = request.POST.get('Basophils')
        temp['CRP'] = request.POST.get('CRP')
        temp['AST'] = request.POST.get('AST')
        temp['ALT'] = request.POST.get('ALT')
        temp['ALP'] = request.POST.get('ALP')
        temp['GGT'] = request.POST.get('GGT')
        temp['LDH'] = request.POST.get('LDH')
    testData = pd.DataFrame({'x':temp}).transpose() 
    scoreval = reloadModel.predict(testData)[0] 
    if(scoreval == 0):
        message = 'POSITIVE'  
    else:
        message = 'NEGATIVE'    
    context={'RESULT':message}
    return render(request, 'index.html',context)
