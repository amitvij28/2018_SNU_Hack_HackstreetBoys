# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl

def laptop_price():
    # Importing the dataset
    dataset = pd.read_csv('./ML_DELL/laptop_prices/laptops_ml.csv')
    X = dataset.iloc[:,[1,2,3,4,5,7,8,9] ].values
    y = dataset.iloc[:, 10].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting Multiple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    # plt.plot(y_pred)
    # plt.plot(y_test,color='red')

    testarr=[]
    for i in range(len(y_test)):
        a=[]
        a.append(i)
        a.append(y_test[i])
        testarr.append(a)
    
    predictarr=[]
    for i in range(len(y_pred)):
        a=[]
        a.append(i)
        a.append(y_pred[i])
        predictarr.append(a)

    return {
        'test':testarr,        
        'predictions':predictarr
    }

