import pandas as pd
import os
import plotly.express as px
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



Recover.write_html("/Django/myapp/static/assets/images/background7.html")
Recover.write_html("/Django/myapp/assets/assets/images/background7.html")

Dead.write_html("/Django/myapp/static/assets/images/background8.html")
Dead.write_html("/Django/myapp/assets/assets/images/background8.html")


Cases.write_html("/Django/myapp/static/assets/images/background6.html")
Cases.write_html("/Django/myapp/assets/assets/images/background6.html")


if os.path.exists('data.csv'):
    os.remove("data.csv")
    os.remove(death_csv)
    os.remove(recovered_csv)
    os.remove(allData)
    os.remove(Date_csv)
    