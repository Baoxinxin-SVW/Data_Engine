import pandas as pd
from efficient_apriori import apriori as apr

data_csv = pd.read_csv('./project_b_data.csv',encoding='gbk')
client_data = data_csv.sort_values(by='客户ID',ascending = True)
client_product = client_data.set_index('客户ID')['产品型号名称']

#合并ID相同客户的产品型号名称为一条，并放入测试集
transactions = []
temp_index = 0

for i, v in client_product.items():
    if i != temp_index:
        temp_set = set()
        temp_index = i
        temp_set.add(v)
        transactions.append(temp_set)
    else:
        temp_set.add(v)


#调用apriori算法
itemsets, rules = apr(transactions, min_support=0.05,  min_confidence=0.2)
temp={}
temp['Transactions'],temp['频繁项集'],temp['关联规则'] = transactions,itemsets,rules

# 定义输出标题
df = pd.DataFrame(columns=['Transactions','频繁项集','关联规则'])
df = df.append(temp,ignore_index = True)
# 打印输出结果的两种方式：
# 控制台输出：
print(transactions)
print('\n频繁项集：')
print(itemsets)
print('\n关联规则：')
print(rules)
# 把分析结果存储到当前目录下的 project_b_result.csv 文件中(此种方法有点小问题，会出现文件未全部加载)
df.to_csv('./project_b_result.csv',index = False,encoding='utf_8_sig')