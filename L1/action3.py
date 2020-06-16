import pandas as pd
from pandas import Series,DataFrame
result = pd.DataFrame(pd.read_csv('car_complain.csv')) #加载
result = result.drop('problem', 1).join(result.problem.str.get_dummies(',')) #  离散的特征处理
df = result.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False) #品牌投诉总数，按照brand对ID进行计数，从大到小排列
df1 = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=False) #车型投诉总数
df2 = result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False) #品牌的平均车型投诉
print(df)
print(df1)
print('平均车型投诉最多的品牌是',df2.iloc[0].name )