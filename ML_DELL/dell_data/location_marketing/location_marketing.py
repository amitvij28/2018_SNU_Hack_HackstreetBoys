# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl

def location_marketing():
    # Importing the dataset
    dataset = pd.read_csv('./ML_DELL/dell_data/location_marketing/dsf.csv')
    X = dataset.iloc[:, [0, 5]].values
    y = dataset.iloc[:, 9].values

    # Encoding categorical data
    # Encoding the Independent Variable
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:, 1] = labelencoder_X.fit_transform(X[:, 1])

    onehotencoder = OneHotEncoder(categorical_features = [1])
    X = onehotencoder.fit_transform(X).toarray()
    X=X[:,1:]

    X=X[:,:3]
    # Encoding the Dependent Variable
    labelencoder_y = LabelEncoder()
    y = labelencoder_y.fit_transform(y)

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

    # Fitting K-NN to the Training set
    from sklearn.neighbors import KNeighborsClassifier
    classifier_KNN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    classifier_KNN.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier_KNN.predict(X_test)
        
    accuracy =0
    for i in range(len(y_pred)):
        if y_test[i]== y_pred[i]:
            accuracy=accuracy+1

    # Fitting K-NN to the Training set
    from sklearn.neighbors import KNeighborsClassifier
    classifier_KNN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    classifier_KNN.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier_KNN.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    accuracy =0
    for i in range(len(y_pred)):
        if y_test[i]== y_pred[i]:
            accuracy=accuracy+1
            
    label_array = ['Recommended','Offline Ads','Social Networks','Tech Blogs']

    #labelencoder_y.inverse_transform(y_test)

    #test=pd.DataFrame(y_test)
    #pred=pd.DataFrame(y_pred)
    #frames=[test,pred]
    #result = pd.concat([test, pred], axis=1, sort=False)
    #result.to_csv('final.csv')


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



