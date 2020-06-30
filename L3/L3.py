import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
   
#轮廓系数
def best(train,row):
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    from sklearn import metrics 
    flag = 2
    SCS_best = -1
    for i in range(2,row+1):
        kmeans = KMeans(n_clusters= i,max_iter=300)
        kmeans.fit(train)
        predict = kmeans.predict(train)
        SCS_now = metrics.silhouette_score(train, predict, metric='euclidean')
        #print("分为%d组时，轮廓系数为%s"%(i,SCS_now))
        if SCS_now > SCS_best:
            SCS_best = SCS_now
            flag = i
    print("最佳分组是分为：%d 组"%(flag))

#K means
def KMeans(data,train,num):
    from sklearn.cluster import KMeans
    from sklearn import preprocessing
    kmeans = KMeans(n_clusters= num,max_iter=300)
    kmeans.fit(train)
    predict_x = kmeans.predict(train)
    result_x = pd.concat((data,pd.DataFrame(predict_x)),axis=1)
    print(result_x)
#层次聚类
def Aggl(data,train,num):
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
    
    best(train_x,row)
    num = int(input("你想分为多少组:"))
    
    if num > row:
        print("分组数太多")
    elif num < 0:
        print("不能为负值")
    else:
        x = int(input("1.K-means,2.层次聚类"))
        if x == 1:
            KMeans(data,train_x,num)
        elif x == 2:
            Aggl(data,train_x,num)
        else:
            print("not def")

if __name__ == '__main__':
    main()    
