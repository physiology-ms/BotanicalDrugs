# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:45:05 2017

@author: physiology

본초학 교과서의 feature를 매개로 feature간의 연결을 정의하여 topology를 만드는 코드

조정변수 : a, b, cut-off

"""
## a,b는 비교국가
a='korea'
b='japan'
## n = permutition 횟수 
n=100000


import os
os.chdir(r'C:\Users\physiology\Desktop\paper')


# numpy, pandas, matplotlib library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

# 폰트 library 불러오기
#from matplotlib import font_manager, rc
#font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/Malgun.ttf").get_name()
#rc('font', family=font_name)

import scipy
import scipy.stats
from scipy import polyval 

import logging, sys
from matplotlib.colors import Normalize
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.transforms as transforms
from gseapy.parser import unique      
import networkx as nx


#    a = input('nation? : ')
#    b = input('another nation? : ')
rawdata = pd.read_excel('botanical data.xlsx', sheetname = a + ' per resample') 
rawdata2 = pd.read_excel('botanical data.xlsx', sheetname = b + ' per resample') 
realdata = pd.read_excel('real intersection data.xlsx', sheetname = a+' '+b)

if a == 'japan':
    nationdata1 = rawdata.ix[:,4:11]
elif a == 'korea':
    nationdata1 = rawdata.ix[:,4:7]
elif a == 'china':
    nationdata1 = rawdata.ix[:,4:9]

if b == 'japan':
    nationdata2 = rawdata2.ix[:,4:11]
elif b == 'korea':
    nationdata2 = rawdata2.ix[:,4:7]
elif b == 'china':
    nationdata2 = rawdata2.ix[:,4:9]
        
booleandata = rawdata.ix[:,11:]
    
feature = booleandata.columns
# column 이름을 튜플 구조로 저장
feature = tuple(feature)
    
nationdata1 = np.array(nationdata1)
nationdata1 = np.transpose(nationdata1) # (일본 기준) 7 * 본초 수

nationdata2 = np.array(nationdata2)
nationdata2 = np.transpose(nationdata2)
    
booleandata = np.array(booleandata) # 본초수 * 69
#booleandata = np.transpose(booleandata) # 69feature * 본초수
    
realdata = realdata.ix[:,1:]
realdata = np.array(realdata)

# data를 평균 + 비율화
nationdata1 = np.sum(nationdata1, axis=0)/nationdata1.shape[0]
nationdata1 = nationdata1/np.sum(nationdata1) 

nationdata2 = np.sum(nationdata2, axis=0)/nationdata2.shape[0]
nationdata2 = nationdata2/np.sum(nationdata2)




cutoff = 10
topology = np.dot(booleandata.T, booleandata)
topology[topology<cutoff] = 0
topology[topology>=cutoff] = 1
np.fill_diagonal(topology, 0)


topology_graph = nx.Graph()

for j, elementj in enumerate(topology):
    for k, elementk in enumerate(elementj):
        if elementk == 1:
            topology_graph.add_edge(j,k)

node1 = []
node2 = []
for i in topology_graph.edges():
    node1.append(i[0])
    node2.append(i[1])

os.chdir(r'./topology')
topology_graph_df = pd.DataFrame({"feature1":node1, "feature2":node2})
topology_graph_df.to_excel("topology_graph_cutoff_"+str(cutoff)+".xlsx")

feature_df = pd.DataFrame({"name":feature})
feature_df = feature_df.reset_index()
feature_df.to_excel("topology_feature_cutoff_"+str(cutoff)+".xlsx")

"""
10.05 나라 별 feature 가중치 추가
"""
weight1 = np.zeros((len(feature),1))
weight2 = np.zeros((len(feature),1))
                   
for k in range(len(feature)):    
    test1 = nationdata1[booleandata[:,k] == 1]    
    test1 = np.sum(test1)    
    weight1[k] = test1 
    
    test2 = nationdata2[booleandata[:,k] == 1]   
    test2 = np.sum(test2)    
    weight2[k] = test2   
    
weight1 = pd.DataFrame(weight1)
weight2 = pd.DataFrame(weight2)

weight1.to_excel("weight_cutoff_"+str(cutoff)+a+".xlsx")
weight2.to_excel("weight_cutoff_"+str(cutoff)+b+".xlsx")
