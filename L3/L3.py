import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, ward 
from sklearn.cluster import KMeans, AgglomerativeClustering 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn import preprocessing

#K means
def KMeans(train,num):
    from sklearn.cluster import KMeans
    from sklearn import preprocessing 
    kmeans = KMeans(n_clusters= num,max_iter=300) 
    kmeans.fit(train) 
    predict = kmeans.predict(train) 
    result = pd.concat((data,pd.DataFrame(predict)),axis=1) 
    print(result)
#层次聚类
def Aggl(train,num):
    model = AgglomerativeClustering(linkage='ward', n_clusters= num) 
    predict = model.fit_predict(train) 
    result = pd.concat((data,pd.DataFrame(predict)),axis=1)
    print(result)
    linkage_matrix = ward(train) 
    dendrogram(linkage_matrix) 
    plt.show() 
#main
def main():
    data = pd.read_csv('car_data.csv',encoding='gbk')
    train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]
    min_max_scaler=preprocessing.MinMaxScaler() 
    train_x=min_max_scaler.fit_transform(train_x) 
    row = train_x.shape[0]-1
    num = int(input("input the number you want to divide:"))
    if num > row:
        print("too many classify")
    elif num < 0:
        print("could not be negative")
    else:
        x = int(input("chose: 1.K-means,2.层次聚类"))
        if x == 1:
            KMeans(train_x,num)
        elif x == 2:
            Aggl(train_x,num)
        else:
            print("not def")


if __name__ == '__main__':
    main()