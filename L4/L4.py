import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from efficient_apriori import apriori
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#apriori
def tryapr(data):
    from efficient_apriori import apriori #为什么：此处若无该语句，即不在函数内使用import，执行会报错：apriori() got an unexpected keyword argument 'min_confidence'
    transactions = []
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, dataset.shape[1]):
            if str(dataset.values[i, j]) != 'nan':
               temp.append(str(dataset.values[i, j]))
        transactions.append(temp)
    itemsets, rules = apriori(transactions, min_support=0.05,  min_confidence=0.2)
    print("*"*20,'频繁项集','*'*20)
    print(itemsets)
    print("*"*20,'关联规则','*'*20)
    print(rules)

    
#mlxtend
def trymlx(data):
    result =pd.DataFrame(columns=('id','buy'))
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, dataset.shape[1]):
            if str(dataset.values[i, j]) != 'nan':
               temp.append(str(dataset.values[i, j]))
        temp = "/".join(temp)
        result=result.append(pd.DataFrame({'id':[i],'buy':[temp]}),ignore_index=True)
    #print(result)
    result_hot_encoded = result.drop('buy',1).join(result.buy.str.get_dummies('/'))
    result_hot_encoded.set_index(['id'],inplace=True)
    #print(result_hot_encoded)
    itemsets = apriori(result_hot_encoded, use_colnames=True,min_support=0.05)
    itemsets = itemsets.sort_values(by="support",ascending=False)
    print("*"*20,'频繁项集','*'*20)
    print(itemsets)
    rules =  association_rules(itemsets, metric='lift', min_threshold=1)
    rules = rules.sort_values(by="lift",ascending=False)
    print("*"*20,'关联规则','*'*20)
    print(rules)

    
def main():
    dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
    a = int(input("选择使用的算法：1.apriori，2.mlxtend\n"))
    if a == 1:
        tryapr(dataset)
    elif a == 2:
        trymlx(dataset)
    else:
        print("无效输入")

    
if __name__ == '__main__':
    main()