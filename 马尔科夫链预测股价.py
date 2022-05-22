# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:15:58 2022

@author: Administrator
"""

import datetime
import numpy as np
import pandas as pd
from matplotlib import cm, pyplot as plt
from hmmlearn.hmm import GaussianHMM

#数据处理
df = pd.read_excel("stto.xlsx", header=0)

wanke=df['收盘价'][1:] #取Excel的第一列

H=np.zeros((len(wanke),1))
for i in range(len(wanke)-1):
    if wanke[i+2]>wanke[i+1]:
       H[i][0]=1 #股票价格上涨取1
    else:
       H[i][0]=0 #股票价格下跌取0
   #上涨为1下跌为0

uu=0
ud=0
du=0
dd=0 
for i in range(len(H)-1):
    if H[i][0]==1 and H[i+1][0]==1:
        uu=uu+1 #统计从上涨到上涨的次数，即在H(i,1)=1的情况下，H(i+1,1)还是等于1  
    elif H[i][0]==1 and H[i+1][0]==0:
        ud=ud+1 #同理，统计从上涨到下跌的次数；
    elif H[i][0]==0 and H[i+1][0]==1:   
        du=du+1 #同理，统计从下跌到上涨的次数；
    elif H[i][0]==0 and H[i+1][0]==0:   
        dd=dd+1 #同理，统计从下跌到下跌的次数；


P=np.matrix([[uu/(uu+ud),ud/(uu+ud)],[du/(du+dd),dd/(du+dd)]]) #作相应的比值，构建转移矩阵

chushi=np.transpose([sum(H)/(len(H)-1),1-sum(H)/(len(H)-1)]) #得出的是初始矩阵
zhuangtai =chushi*P