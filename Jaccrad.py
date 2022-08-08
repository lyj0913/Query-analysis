# encoding=utf8
# !/usr/bin/python
import sys
import json

def Jaccrad(model, reference):#terms_reference为源句子，terms_model为候选句子
    terms_reference= list(reference)#精准模式
    terms_model= list(model)
    grams_reference = set(terms_reference)#去重；如果不需要就改为list
    grams_model = set(terms_model)
    temp = 0
    for i in grams_reference:
        if i in grams_model:
            temp=temp+1
    fenmu=len(grams_model)+len(grams_reference)-temp #并集
    jaccard_coefficient=float(temp/fenmu)#交集
    return jaccard_coefficient
