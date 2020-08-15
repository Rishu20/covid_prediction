import pandas as pd
import os
import plotly.express as px
import csv
import sklearn
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime
from threading import Timer
from Covid_Data import *

numfile = "num.csv"
total_csv= "confirm.csv"
death_csv = "Death.csv"
recovered_csv = "recovered.csv"
allData = "alldata.csv"
Date_csv = "Date.csv"


df = pd.read_csv('Data.csv')


Cases = px.line(df, x = 'Day', y = 'Total Case', title='Total Case')

Dead = px.line(df, x = 'Day', y = 'Dead', title='Death')

Recover = px.line(df, x = 'Day', y = 'Recover', title='Recover')



Recover.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/static/assets/images/background7.html")
Recover.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/assets/assets/images/background7.html")

Dead.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/static/assets/images/background8.html")
Dead.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/assets/assets/images/background8.html")


Cases.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/static/assets/images/background6.html")
Cases.write_html("C:/Users/susha/Programmings/Programs/Django/myapp/assets/assets/images/background6.html")


if os.path.exists(death_csv):
    os.remove(death_csv)
    os.remove(recovered_csv)
    os.remove(allData)
    os.remove(Date_csv)
    