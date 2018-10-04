# coding: utf-8
import pandas
data=pandas.read_csv('housing_oslo.csv')
data.head()
X=data.drop('Price',1)
X.head(2)
Y=data['Price']
Y.head(2)
import sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X,Y,random_state=0)
X_train.head(2)
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,y_train)
import numpy
new_data_item=numpy.array([[168,202,4,3,4,2014,0,171,1,1]])
regression.predict(new_data_item)
