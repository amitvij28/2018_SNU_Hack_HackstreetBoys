from pandas import read_csv


def get_data_pc():
    
    dataset = read_csv('./productconfig/laptop_price.csv')
    X  = dataset.iloc[:,0].tolist()
    Y1=dataset.iloc[:,1].tolist()
    Y2 = dataset.iloc[:,2].tolist()

    var = 0
    Arr1=[]
    for i in range(len(X)):
        a=[]
        a.append(X[i])
        a.append(Y1[i])
        Arr1.append(a)
        
    Arr2=[]
    for i in range(len(X)):
        a=[]
        # if var%2 == 0:
        #     if Y1[i] == 4:
        #         Y2[i]=4
        a.append(X[i])
        a.append(Y2[i])
        Arr2.append(a)
        var+=1
    
    Arr1 = Arr1[:300]
    Arr2=Arr2[:300]

    return {
        'Arr1':Arr1,
        'Arr2':Arr2
    }

