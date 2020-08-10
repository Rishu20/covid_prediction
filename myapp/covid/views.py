from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.path.insert(1, 'C:/Users/susha/Programmings/Programs/Django/myapp/covid/covid_ml')
from mlbase import *
# Create your views here.

def input(request):
    return render(request, 'input.html')

def result(request):
    dd = int(request.POST["DD"])
    mm = int(request.POST["MM"])
    yy = int(request.POST["YY"])
    year = yy
    month = mm
    day = dd
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

        x_Days=[[m]]
        predict = (int(model.predict(poly_reg.fit_transform(x_Days))))
    elif b < 0:
        predict = ("Sorry I can't predict past")
    else:
        predict = ("Sorry invalid input")

    res = predict
    return render(request, "result.html", {'result':res})