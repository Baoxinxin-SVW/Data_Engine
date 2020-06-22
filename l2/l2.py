import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

#url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
#html = requests.get(url)
#html_page = html.text
#soup = BeautifulSoup(html_page,'html.parser')

def analysis(soup):
	temp = soup.find('div',class_='tslb_b')
	df = pd.DataFrame(columns=['id','brand','car_model','type','descrption','problem','daytime','status'])
	reg = re.compile(("<[^>]*>"))
	tr_list = temp.find_all('tr')
	for tr in tr_list:
		temp = {}
		td_list = tr.find_all('td')
		print(td_list)
		if len(td_list) > 0:
			id = reg.sub('',str(td_list[0]))
			brand = reg.sub('',str(td_list[1]))
			car_model = reg.sub('',str(td_list[2]))
			type = reg.sub('',str(td_list[3]))
			descrption = reg.sub('',str(td_list[4]))
			problem = reg.sub('',str(td_list[5]))
			daytime = reg.sub('',str(td_list[6]))
			status = reg.sub('',str(td_list[7]))
			temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['descrption'],temp['problem'],temp['daytime'],temp['status']=id,brand,car_model,type,descrption,problem,daytime,status
			df = df.append(temp,ignore_index = True)
		return df

##df = analysis(soup)
##print(df)

def get_page_content(request_url):
	html = requests.get(request_url)
	html_page = html.text
	soup = BeautifulSoup(html_page,'html.parser')
	return soup


result = pd.DataFrame(columns=['id','brand','car_model','type','descrption','problem','daytime','status'])
page_num = 20
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'

for i in range(page_num):
	request_url = base_url + str(i+1)+'.shtml'
	soup = get_page_content(request_url)
	df = analysis(soup)
	print(df)
	result = result.append(df)

result.to_csv('result.csv',index = False,encoding='utf_8_sig')