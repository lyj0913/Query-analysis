#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


data=pd.read_csv("dictionary_2.txt",encoding='utf-8',sep='\t',header=None)
data.columns = ['keyword','location','type']
data1 = data[data['location']=='1']


data2=pd.read_csv("v1.csv",encoding='utf-8',sep=',',header=None)
data2.columns=['query','pv']
data2 = data2.drop(data2.index[range(1)])
data2 = data2[['query']] # keep the needed column

#交集query
cond = data2['query'].isin(data1['keyword'])
inner_df = data2[cond]
inner_df.to_csv('交集的query.csv')


#diff1_query(data1去掉交集所剩query,data2缺失部分)
diff1 = data1
cond = diff1['keyword'].isin(inner_df['query'])
diff1.drop(diff1[cond].index, inplace = True)
diff1.to_csv('diff1_query.csv')


#diff2_query(data2去掉交集所剩query, data1缺失部分)
diff2 = data2
cond = diff2['query'].isin(inner_df['query'])
diff2.drop(diff2[cond].index,inplace=True)
diff2.to_csv('diff2_query.csv')


diff1.sample(n=10) #check diff1

diff2.sample(n=10) #check diff2
