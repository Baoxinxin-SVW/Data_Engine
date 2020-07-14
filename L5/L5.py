# -*- coding:utf-8 -*-
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

# 本习题中无停用词
# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 数据加载
dataset = pd.read_csv('./Market_Basket_Optimisation.csv',header=None)
#print(data)
temp=[]
all_word=""
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(str(dataset.values[i, j]))
    temp = " ".join(temp)
    all_word=all_word+temp
create_word_cloud(all_word)