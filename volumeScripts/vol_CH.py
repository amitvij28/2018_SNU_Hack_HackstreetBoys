#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 03:00:03 2018

@author: atishay
"""

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

def modelrunCH():
    series = read_csv('laptop_sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
    series = series['china'].resample('MS').mean()
    #print(series)
    err=[]
    X = series.values
    #print(len(X))
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        #print('predicted=%f, expected=%f' % (yhat, obs))
        err.append(abs(yhat-obs))
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    print('Bias: ', sum(err)/len(test))
    return {
        'test':test,
        
        'predictions':predictions
    }


# plot
# pyplot.figure(0)
# pyplot.plot(test)
# pyplot.plot(predictions, color='red')
# #pyplot.figure(1)
# #pyplot.plot(err, color='green')
# pyplot.show()