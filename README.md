# Toyota Tacoma Value Estimator
## Summary

A web application built with the Python programming language using the Flask 
web framework. The raw dataset was in the form of a csv file and the Pandas library was used to 
clean and manipulate the data. Scikit-learn library was used to build, train and test the 
machine learning model which was used to estimate the price of the used vehicles. The Dash 
framework was used to generate the visualizations and the whole web application was 
deployed on the Heroku cloud platform. 


## Dataset

The dataset used to train the model was obtained from Kaggle.com 
(https://www.kaggle.com/austinreese/craigslist-carstrucks-data). The data was in a csv file of 
size 1.42GB with 25 attributes and over 500,00 entries. It contained every used vehicle entry in 
the United States from Craigslist.com. Irrelevant attributes were dropped: Entries with zero and missing
values were removed and only entries with Toyota Tacomas were kept
 
 
## Machine Learning

The model was trained by 80% of the data, the rest 20% was tested using the model’s 
default scoring function. The Gradient Boosting Regressor was trained with other machine 
learning models. The most accurate model was the GBR with the accuracy score of 86.73% 
It can be trained in the models.py file. There are inputs available in the home page for the factors and 
specification of the vehicle which will be used by the model to estimate the price of the vehicle. 

![mltraining](/images/mltrain.png)

## Visualizations

Data visualizations are available in the [Visualizations](http://github.com) page. 

## User Guide

* The web application can be accessed by clicking on this [link](https://tacoma-estimator.herokuapp.com/).
* You will be directed to the login page:

![login](/images/login.png)

* The username is ‘test’ and the password is ‘test’.
* You will then be directed to the homepage:

![home](/images/homepage.png)

* You can enter information about the specifications of the vehicle you want to predict. Click on estimate to get an estimate of the vehicle’s price.
* You can also Logout or go to the visualizations page by clicking on the visualizations button on the upper left corner.

![visual](/images/visual.png)









