#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

new_data=pd.read_csv("sim_score4.csv",encoding='utf-8',sep='\t',header=None)
new_data.columns = ['keyword']


#地区-地点
district=pd.read_csv("district.txt",encoding='utf-8',sep='\t',header=None)
district.columns = ['0','1','2','3','4','5','6','7','8','9','10']
district = district[['1']]
district.columns = ['district']
#镇区-名称
location=pd.read_csv("镇区.txt",encoding='utf-8',sep='\t',header=None)
location.columns = ['locate','idk']
location = location[['locate']]
loc = location[location["locate"].str.endswith("镇")]
loc['locate'] = loc['locate'].str[:-1]
#县
location_xian=pd.read_csv("loc_xian.txt",encoding='utf-8',sep=',',header=None)
location_xian.columns = ['idk','locate']
location_xian = location_xian[['locate']]


new_data[new_data["keyword"].str.contains("^市|^县")]['keyword']


shi_data = pd.Series()
qu_data = pd.Series()
diqu_data = pd.Series()
sheng_data = pd.Series()
de_data = pd.Series()
obj_data = pd.Series()

#去掉第一个字（市/县/区/地区/省/的）
shi_data['keyword']= new_data[new_data["keyword"].str.contains("^市|^县")]['keyword'].map(lambda x: str(x)[1:])
shi_data = pd.DataFrame(shi_data['keyword'])
qu_data['keyword'] = new_data[new_data["keyword"].str.contains("^区")]['keyword'].map(lambda x: str(x)[1:])
qu_data = pd.DataFrame(qu_data['keyword'])
diqu_data['keyword'] = new_data[new_data["keyword"].str.contains("^地区")]['keyword'].map(lambda x: str(x)[2:])
diqu_data = pd.DataFrame(qu_data['keyword'])
sheng_data['keyword'] = new_data[new_data["keyword"].str.contains("^省")]['keyword'].map(lambda x: str(x)[1:])
sheng_data = pd.DataFrame(sheng_data['keyword'])
de_data['keyword'] = new_data[new_data["keyword"].str.contains("^的")]['keyword'].map(lambda x: str(x)[1:])
de_data = pd.DataFrame(sheng_data['keyword'])


new_data1= new_data.append(shi_data)
new_data1 = new_data1.append(qu_data)
new_data1 = new_data1.append(diqu_data)
new_data1 = new_data1.append(sheng_data)
new_data1 = new_data1.append(de_data)
new_data1 = new_data1.append(obj_data)


dist = '|'.join(district['district'].tolist())
dist_loc = '|'.join(location['locate'].tolist())
dist_xian = '|'.join(location_xian['locate'].tolist())
dist_zhen = '|'.join(loc['locate'].tolist())


#drop datas
drop_needed = new_data[new_data["keyword"].str.contains(dist)]
cond = new_data['keyword'].isin(drop_needed['keyword'])
new_data.drop(new_data[cond].index,inplace=True)


#labeling
data1['label'] = np.where(data1['keyword'].str.contains("x|y|z"), '1', '2')
#check label cnts
data1[data1['label']=='1']
