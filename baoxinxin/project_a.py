import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# 被分析大众车辆信息的URL（此URL是大众中SUV的连接）
url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
html = requests.get(url)
html_page = html.text
html_parser = BeautifulSoup(html_page,'html.parser')

car_info_list = html_parser.find('div',class_="search-result-list")
# 定义输出标题
df = pd.DataFrame(columns=['车辆名称','最低价格(万)','最高价格(万)','车辆图片'])
# 获取车辆信息的集合
car_list = car_info_list.find_all('div',class_='search-result-list-item')

# 循环取出符合条件的标签
for item in car_list:
    temp={}
    #取车型名称
    name = item.find('p',class_='cx-name text-hover').text
    #取价格，如果结果为暂无，则最低价，最高价皆为暂无，否则以‘-’符号进行分隔，然后取出最低价和最高价
    price = item.find('p',class_='cx-price').text
    if price == '暂无':
        low_price = '暂无'
        high_price = '暂无'
    else:
        price = price.replace('万','')
        low_price = re.split('-',price)[0]
        high_price = re.split('-',price)[1]
    #取图片地址
    img_ = 'http:'+item.find(name='img').get('src')
    #装入df中
    temp['车辆名称'],temp['最低价格(万)'],temp['最高价格(万)'],temp['车辆图片'] = name,low_price,high_price,img_
    df = df.append(temp,ignore_index = True)
# 控制台打印分析的结果
print(df)
# 把分析结果存储到当前目录下的 project_a_result.csv 文件中
df.to_csv('./project_a_result.csv',index = False,encoding='utf_8_sig')