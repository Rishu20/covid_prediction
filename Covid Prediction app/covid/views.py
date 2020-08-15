from django.shortcuts import render
import re
from django.http import HttpResponse
import sys
sys.path.insert(1, 'C:/Users/susha/Programmings/Programs/Django/myapp/covid/covid_ml')
from Ml_Base import *

# Create your views here.

def input(request):
    return render(request, 'input.html')


def result(request):
    dd = request.POST["DD"]
    mm = request.POST["MM"]
    yy = request.POST["YY"]
    
    year = int(yy)
    month = int(mm)
    day = int(dd)

    import datetime
    from datetime import date

    d1 = datetime.date(year, month, day)
    d2 = date.today()
    today = d1 - d2
    b = int(today.days)
    n = row_count
    
    poly_reg=PolynomialFeatures(degree=2)
    X=poly_reg.fit_transform(Days)
    model=linear_model.LinearRegression()
    model.fit(X,Cases)


    if b > 0:
        if b >= 10:
            m = ((n+14.5)+b)
        elif b >=4 :
            m =((n+11)+b)
        else:
            m = ((n+9.9)+b)

        
        Dat = on + " " + dd + dev + mm + dev + yy + " " + bt

        x_Days=[[m]]
        predict = int(model.predict(poly_reg.fit_transform(x_Days)))
        pre = str(predict)
        Dat = on + " " + dd + dev + mm + dev + yy + " " + bt + " "+ pre
        res = Dat

    elif b <= 0:
        predict = ("!!!!! Sorry I can't predict past !!!!!")
        res = str(predict)

    else:
        predict = ("Sorry invalid input")
        #res = str(predict)

    return render(request, "result.html", {'result':res})

