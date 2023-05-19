# Covid Prediction

<p>The short-term COVID-19 prediction model project involves fetching and organizing the daily COVID-19 cases data
    for India using the Pandas library. The project fetches the data from the CSSEGISandData repository and stores it
    in a tidy format in a CSV file named "India.csv". The <code>loadData</code> function is used to convert the raw
    data into a tidy format for confirmed cases, deaths, and recovered cases. The <code>refreshData</code> function
    merges the three dataframes, keeps only the data for India, and adds a new column named "Day" representing the
    number of days since the first case was reported in India.</p>
  <p>The organized data can be used to develop a short-term prediction model using linear regression. By using the
    "Day" column as the independent variable and the "CumConfirmed" column as the dependent variable, the model can
    predict the number of COVID-19 cases for upcoming days. However, it's important to keep in mind that the
    accuracy of the model may be impacted by changes in testing protocols, vaccination rates, and government
    policies. Overall, this project offers a useful tool for analyzing COVID-19 cases data and developing predictive
    models for India.</p>

### A Fully Automated Django Based covid-india Prediction App Which Fetch The Database Then Performs Necessary Calculations On The Data Using The Skit-learn Library Then Push Everything To The Frontend UI
### Built Using the [CSSEGISandData](https://github.com/CSSEGISandData/COVID-19) COVID Database
### Use This [Link](https://shushantrishav.pythonanywhere.com/covid) To See The app In action
![screenshot](https://github.com/Rishu20/covid_prediction/blob/web/Covid%20Prediction%20app/assets/assets/images/Annotation%202020-08-15%20123909.png)
