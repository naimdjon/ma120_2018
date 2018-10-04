## Exercise 5. Supervised learning.
Part 1.  Predicting Oslo housing prices.
---
In this exercise you will predict the housing price of a real estate in Oslo. The dataset has been carefully collected from the Norwegian website finn.no. You will find the dataset in Its Learning under the exercise 5 folder.

1. ```docker run -d --rm --name scikit -p 8888:8888 -v `pwd`:/code smizy/scikit-learn```

1. drop in the shell of the container:
`docker exec -it scikit sh`
1. For the examples, the recommended shell to use is `ipython`, i.e. execute `ipython console`. Alternatively, use jupyter notebook. Check the log of the docker container with `docker logs scikit`, you will see the url at the bottom. Open it in your browser, and on the top right, you have dropdown with the choice of "New => python3".
1. Load the file `housing_oslo.csv`. Also available from the following url: http://j.mp/2DOgo2 (if you cannot map the volume, you can use `wget` to download the file while you are inside the container).
   Remember to import the following libraries:
```
    import pandas # Python Data Analysis Library
    import matplotlib.pyplot as plt # For creating plots
    from sklearn.linear_model import LinearRegression # the machine learning model to be used
    from sklearn.model_selection import train_test_split # helper function to split the dataset
```
Use  `pandas.read_csv` to load the data and assign it to a variable, e.g. `data`.
Check the type of the variable using `type(data)`. This data type is described as and is always used when you read a csv file:
> Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.
1. Check the features:
    `data.head(0)`
1. We need to extract the Price column and assign it to Y; this is our prediction value, and the features must not include it, it is rather the target our model will learn:
    ```
       X=data.drop('Price',1)
       Y=data['Price']
    ```
1. We use the helper function `train_test_split` to split the dataset into a training set and a test set:
```
X_train, X_test, y_train, y_test = train_test_split(X,Y,random_state=0)
```
1. Check the size of training and test sets using the `.shape`.
1. Create your model:
  `lm = LinearRegression()`
1. Fit your model:
   `regression=lm.fit(X_train,y_train)`
Remember, we are using the the training sets  here both for features and targets.
1. Calculate score.
    `score=regression.score(X_test,y_test)`

**Predicting prices for new examples.**  
Go to finn.no and find a property (section eiendom). You need the following properties:  
FloorSpace  - Primærrom  
UsableArea  - Bruttoareal  
Rooms  
Bedrooms  
Type  
YearBuilt  
Floor  (mostly for appartments, for houses used 0)  
Tomt  
Parking  
OwnershipType  

**Type**:  
Leilighet=>1  
Enebolig=>2  
Rekkehus=>3  
Tomannsbolig=>4  

**OwnershipType**:  
Selveier=>1  
Andel=>2  

**Parking**:  
HasOwnParking=>1  
DoesNotHaveOwnParking=>2  

**Tomt**:  
Land area

Create a csv string for the new example, e.g.:
```
Price,FloorSpace,UsableArea,Rooms,Bedrooms,Type,YearBuilt,Floor,Tomt,Parking OwnershipType
0,200,215,4,3,2,1915,0,1214,1,1
```

Try to predict the price:
```
from io import StringIO # needed to read inline csv, numpy.array() is another alternative
new_data_item=pandas.read_csv(StringIO("""
       FloorSpace,UsableArea,Rooms,Bedrooms,Type,YearBuilt,Floor,Tomt,Parking, OwnershipType
       200,215,4,3,2,1915,0,1214,1,1""")) # finnkode 129292885
price_predicted=regression.predict(new_data_item)
print price_predicted
```

NB! Couple of notes here. This tiny dataset from last year. This affects the results. The tiny dataset is sensitive to the different areas of Oslo. Homes in central Oslo are for example more expensive than those located a bit farther from the downtown.


Part 2. (Homework, a kaggle competition)
---
The part 2 is optional. Using regression techniques, predict sales prices of houses in Ames, Iowa, USA (based on 79 variables). http://bit.ly/2RfHuDA
