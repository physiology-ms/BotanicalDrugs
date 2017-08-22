# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:35:39 2017

@author: physiology
"""

import os
os.chdir(r'C:\Users\physiology\Desktop\paper')

# numpy, pandas, matplotlib library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tk

# 폰트 library 불러오기
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/Malgun.ttf").get_name()
rc('font', family=font_name)

import scipy
import scipy.stats
from scipy import polyval 


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Excel data 불러오기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
data = pd.read_excel('botanical data.xlsx', sheetname = 'union data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
categorydata = data.ix[:,1:53]
namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')

number = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number1 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20)

categorydata = np.array(categorydata)

#해표약
cat1 = (categorydata[:,32] == 1)
cat1 = categorydata[cat1, 3:6]

ca1 = np.array([0,0,0])
for j in cat1:
    ca1 = ca1 + j

#청열약
cat2 = (categorydata[:,33] == 1)
cat2 = categorydata[cat2, 3:6]

ca2 = np.array([0,0,0])
for j in cat2:
    ca2 = ca2 + j
    
# 사하약
cat3 = (categorydata[:,34] == 1)
cat3 = categorydata[cat3, 3:6]

ca3 = np.array([0,0,0])
for j in cat3:
    ca3 = ca3 + j
    
# 거풍습약
cat4 = (categorydata[:,35] == 1)
cat4 = categorydata[cat4, 3:6]

ca4 = np.array([0,0,0])
for j in cat4:
    ca4 = ca4 + j
    
# 방향화습약
cat5 = (categorydata[:,36] == 1)
cat5 = categorydata[cat5, 3:6]

ca5 = np.array([0,0,0])
for j in cat5:
    ca5 = ca5 + j

# 이수삼습약    
cat6 = (categorydata[:,37] == 1)
cat6 = categorydata[cat6, 3:6]

ca6 = np.array([0,0,0])
for j in cat6:
    ca6 = ca6 + j
    
# 온리약
cat7 = (categorydata[:,38] == 1)
cat7 = categorydata[cat7, 3:6]

ca7 = np.array([0,0,0])
for j in cat7:
    ca7 = ca7 + j

# 이기약    
cat8 = (categorydata[:,39] == 1)
cat8 = categorydata[cat8, 3:6]

ca8 = np.array([0,0,0])
for j in cat8:
    ca8 = ca8 + j

# 소식약
cat9 = (categorydata[:,40] == 1)
cat9 = categorydata[cat9, 3:6]

ca9 = np.array([0,0,0])
for j in cat9:
    ca9 = ca9 + j

# 구충약
cat10 = (categorydata[:,41] == 1)
cat10 = categorydata[cat10, 3:6]

ca10 = np.array([0,0,0])
for j in cat10:
    ca10 = ca10 + j

# 지혈약
cat11 = (categorydata[:,42] == 1)
cat11 = categorydata[cat11, 3:6]

ca11 = np.array([0,0,0])
for j in cat11:
    ca11 = ca11 + j

# 활혈거어약
cat12 = (categorydata[:,43] == 1)
cat12 = categorydata[cat12, 3:6]

ca12 = np.array([0,0,0])
for j in cat12:
    ca12 = ca12 + j

# 화담지해평천약
cat13 = (categorydata[:,44] == 1)
cat13 = categorydata[cat13, 3:6]

ca13 = np.array([0,0,0])
for j in cat13:
    ca13 = ca13 + j

# 안신약
cat14 = (categorydata[:,45] == 1)
cat14 = categorydata[cat14, 3:6]

ca14 = np.array([0,0,0])
for j in cat14:
    ca14 = ca14 + j

# 평간약
cat15 = (categorydata[:,46] == 1)
cat15 = categorydata[cat15, 3:6]

ca15 = np.array([0,0,0])
for j in cat15:
    ca15 = ca15 + j

# 개규약
cat16 = (categorydata[:,47] == 1)
cat16 = categorydata[cat16, 3:6]

ca16 = np.array([0,0,0])
for j in cat16:
    ca16 = ca16 + j

# 보익약
cat17 = (categorydata[:,48] == 1)
cat17 = categorydata[cat17, 3:6]

ca17 = np.array([0,0,0])
for j in cat17:
    ca17 = ca17 + j

# 수삽약
cat18 = (categorydata[:,49] == 1)
cat18 = categorydata[cat18, 3:6]

ca18 = np.array([0,0,0])
for j in cat18:
    ca18 = ca18 + j

# 용토약
cat19 = (categorydata[:,50] == 1)
cat19 = categorydata[cat19, 3:6]

ca19 = np.array([0,0,0])
for j in cat19:
    ca19 = ca19 + j

# 외용약
cat20 = (categorydata[:,51] == 1)
cat20 = categorydata[cat20, 3:6]

ca20 = np.array([0,0,0])
for j in cat20:
    ca20 = ca20 + j
    

category1 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca17, ca18, ca19, ca20]
category1 = np.array(category1)
category1 = np.transpose(category1)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category1, cmap=cmap)
plt.colorbar()

categoryexcel = category1[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category union.xlsx')


category11 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca18, ca19, ca20]
category11 = np.array(category11)
category11 = np.transpose(category11)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category11, cmap=cmap)
plt.colorbar()

categoryexcel = category11[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category union without 17.xlsx')

"""
"""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
categorydata = data.ix[:,1:53]
namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')

number = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number1 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20)

categorydata = np.array(categorydata)

#해표약
cat1 = (categorydata[:,32] == 1)
cat1 = categorydata[cat1, 3:6]

ca1 = np.array([0,0,0])
for j in cat1:
    ca1 = ca1 + j

#청열약
cat2 = (categorydata[:,33] == 1)
cat2 = categorydata[cat2, 3:6]

ca2 = np.array([0,0,0])
for j in cat2:
    ca2 = ca2 + j
    
# 사하약
cat3 = (categorydata[:,34] == 1)
cat3 = categorydata[cat3, 3:6]

ca3 = np.array([0,0,0])
for j in cat3:
    ca3 = ca3 + j
    
# 거풍습약
cat4 = (categorydata[:,35] == 1)
cat4 = categorydata[cat4, 3:6]

ca4 = np.array([0,0,0])
for j in cat4:
    ca4 = ca4 + j
    
# 방향화습약
cat5 = (categorydata[:,36] == 1)
cat5 = categorydata[cat5, 3:6]

ca5 = np.array([0,0,0])
for j in cat5:
    ca5 = ca5 + j

# 이수삼습약    
cat6 = (categorydata[:,37] == 1)
cat6 = categorydata[cat6, 3:6]

ca6 = np.array([0,0,0])
for j in cat6:
    ca6 = ca6 + j
    
# 온리약
cat7 = (categorydata[:,38] == 1)
cat7 = categorydata[cat7, 3:6]

ca7 = np.array([0,0,0])
for j in cat7:
    ca7 = ca7 + j

# 이기약    
cat8 = (categorydata[:,39] == 1)
cat8 = categorydata[cat8, 3:6]

ca8 = np.array([0,0,0])
for j in cat8:
    ca8 = ca8 + j

# 소식약
cat9 = (categorydata[:,40] == 1)
cat9 = categorydata[cat9, 3:6]

ca9 = np.array([0,0,0])
for j in cat9:
    ca9 = ca9 + j

# 구충약
cat10 = (categorydata[:,41] == 1)
cat10 = categorydata[cat10, 3:6]

ca10 = np.array([0,0,0])
for j in cat10:
    ca10 = ca10 + j

# 지혈약
cat11 = (categorydata[:,42] == 1)
cat11 = categorydata[cat11, 3:6]

ca11 = np.array([0,0,0])
for j in cat11:
    ca11 = ca11 + j

# 활혈거어약
cat12 = (categorydata[:,43] == 1)
cat12 = categorydata[cat12, 3:6]

ca12 = np.array([0,0,0])
for j in cat12:
    ca12 = ca12 + j

# 화담지해평천약
cat13 = (categorydata[:,44] == 1)
cat13 = categorydata[cat13, 3:6]

ca13 = np.array([0,0,0])
for j in cat13:
    ca13 = ca13 + j

# 안신약
cat14 = (categorydata[:,45] == 1)
cat14 = categorydata[cat14, 3:6]

ca14 = np.array([0,0,0])
for j in cat14:
    ca14 = ca14 + j

# 평간약
cat15 = (categorydata[:,46] == 1)
cat15 = categorydata[cat15, 3:6]

ca15 = np.array([0,0,0])
for j in cat15:
    ca15 = ca15 + j

# 개규약
cat16 = (categorydata[:,47] == 1)
cat16 = categorydata[cat16, 3:6]

ca16 = np.array([0,0,0])
for j in cat16:
    ca16 = ca16 + j

# 보익약
cat17 = (categorydata[:,48] == 1)
cat17 = categorydata[cat17, 3:6]

ca17 = np.array([0,0,0])
for j in cat17:
    ca17 = ca17 + j

# 수삽약
cat18 = (categorydata[:,49] == 1)
cat18 = categorydata[cat18, 3:6]

ca18 = np.array([0,0,0])
for j in cat18:
    ca18 = ca18 + j

# 용토약
cat19 = (categorydata[:,50] == 1)
cat19 = categorydata[cat19, 3:6]

ca19 = np.array([0,0,0])
for j in cat19:
    ca19 = ca19 + j

# 외용약
cat20 = (categorydata[:,51] == 1)
cat20 = categorydata[cat20, 3:6]

ca20 = np.array([0,0,0])
for j in cat20:
    ca20 = ca20 + j
    

category2 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca17, ca18, ca19, ca20]
category2 = np.array(category2)
category2 = np.transpose(category2)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category2, cmap=cmap)
plt.colorbar()

categoryexcel = category2[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jkcjoint.xlsx')


category22 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca18, ca19, ca20]
category22 = np.array(category22)
category22 = np.transpose(category22)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category22, cmap=cmap)
plt.colorbar()

categoryexcel = category22[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jkcjoint without 17.xlsx')


"""
"""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
categorydata = data.ix[:,1:53]
namelist = data.ix[:,0]
nation = ('Japan', 'Korea')

number = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number1 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20)

categorydata = np.array(categorydata)

#해표약
cat1 = (categorydata[:,32] == 1)
cat1 = categorydata[cat1, 3:6]

ca1 = np.array([0,0,0])
for j in cat1:
    ca1 = ca1 + j

#청열약
cat2 = (categorydata[:,33] == 1)
cat2 = categorydata[cat2, 3:6]

ca2 = np.array([0,0,0])
for j in cat2:
    ca2 = ca2 + j
    
# 사하약
cat3 = (categorydata[:,34] == 1)
cat3 = categorydata[cat3, 3:6]

ca3 = np.array([0,0,0])
for j in cat3:
    ca3 = ca3 + j
    
# 거풍습약
cat4 = (categorydata[:,35] == 1)
cat4 = categorydata[cat4, 3:6]

ca4 = np.array([0,0,0])
for j in cat4:
    ca4 = ca4 + j
    
# 방향화습약
cat5 = (categorydata[:,36] == 1)
cat5 = categorydata[cat5, 3:6]

ca5 = np.array([0,0,0])
for j in cat5:
    ca5 = ca5 + j

# 이수삼습약    
cat6 = (categorydata[:,37] == 1)
cat6 = categorydata[cat6, 3:6]

ca6 = np.array([0,0,0])
for j in cat6:
    ca6 = ca6 + j
    
# 온리약
cat7 = (categorydata[:,38] == 1)
cat7 = categorydata[cat7, 3:6]

ca7 = np.array([0,0,0])
for j in cat7:
    ca7 = ca7 + j

# 이기약    
cat8 = (categorydata[:,39] == 1)
cat8 = categorydata[cat8, 3:6]

ca8 = np.array([0,0,0])
for j in cat8:
    ca8 = ca8 + j

# 소식약
cat9 = (categorydata[:,40] == 1)
cat9 = categorydata[cat9, 3:6]

ca9 = np.array([0,0,0])
for j in cat9:
    ca9 = ca9 + j

# 구충약
cat10 = (categorydata[:,41] == 1)
cat10 = categorydata[cat10, 3:6]

ca10 = np.array([0,0,0])
for j in cat10:
    ca10 = ca10 + j

# 지혈약
cat11 = (categorydata[:,42] == 1)
cat11 = categorydata[cat11, 3:6]

ca11 = np.array([0,0,0])
for j in cat11:
    ca11 = ca11 + j

# 활혈거어약
cat12 = (categorydata[:,43] == 1)
cat12 = categorydata[cat12, 3:6]

ca12 = np.array([0,0,0])
for j in cat12:
    ca12 = ca12 + j

# 화담지해평천약
cat13 = (categorydata[:,44] == 1)
cat13 = categorydata[cat13, 3:6]

ca13 = np.array([0,0,0])
for j in cat13:
    ca13 = ca13 + j

# 안신약
cat14 = (categorydata[:,45] == 1)
cat14 = categorydata[cat14, 3:6]

ca14 = np.array([0,0,0])
for j in cat14:
    ca14 = ca14 + j

# 평간약
cat15 = (categorydata[:,46] == 1)
cat15 = categorydata[cat15, 3:6]

ca15 = np.array([0,0,0])
for j in cat15:
    ca15 = ca15 + j

# 개규약
cat16 = (categorydata[:,47] == 1)
cat16 = categorydata[cat16, 3:6]

ca16 = np.array([0,0,0])
for j in cat16:
    ca16 = ca16 + j

# 보익약
cat17 = (categorydata[:,48] == 1)
cat17 = categorydata[cat17, 3:6]

ca17 = np.array([0,0,0])
for j in cat17:
    ca17 = ca17 + j

# 수삽약
cat18 = (categorydata[:,49] == 1)
cat18 = categorydata[cat18, 3:6]

ca18 = np.array([0,0,0])
for j in cat18:
    ca18 = ca18 + j

# 용토약
cat19 = (categorydata[:,50] == 1)
cat19 = categorydata[cat19, 3:6]

ca19 = np.array([0,0,0])
for j in cat19:
    ca19 = ca19 + j

# 외용약
cat20 = (categorydata[:,51] == 1)
cat20 = categorydata[cat20, 3:6]

ca20 = np.array([0,0,0])
for j in cat20:
    ca20 = ca20 + j
    

category3 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca17, ca18, ca19, ca20]
category3 = np.array(category3)
category3 = category3[:,0:2]
category3 = np.transpose(category3)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category3, cmap=cmap)
plt.colorbar()

categoryexcel = category3[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jkjoint.xlsx')


category33 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca18, ca19, ca20]
category33 = np.array(category33)
category33 = category33[:,0:2]
category33 = np.transpose(category33)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 0.15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category33, cmap=cmap)
plt.colorbar()

categoryexcel = category33[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jkjoint without 17.xlsx')


"""
"""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
categorydata = data.ix[:,1:53]
namelist = data.ix[:,0]
nation = ('Japan', 'China')

number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20)

categorydata = np.array(categorydata)

#해표약
cat1 = (categorydata[:,32] == 1)
cat1 = categorydata[cat1, 3:6]

ca1 = np.array([0,0,0])
for j in cat1:
    ca1 = ca1 + j

#청열약
cat2 = (categorydata[:,33] == 1)
cat2 = categorydata[cat2, 3:6]

ca2 = np.array([0,0,0])
for j in cat2:
    ca2 = ca2 + j
    
# 사하약
cat3 = (categorydata[:,34] == 1)
cat3 = categorydata[cat3, 3:6]

ca3 = np.array([0,0,0])
for j in cat3:
    ca3 = ca3 + j
    
# 거풍습약
cat4 = (categorydata[:,35] == 1)
cat4 = categorydata[cat4, 3:6]

ca4 = np.array([0,0,0])
for j in cat4:
    ca4 = ca4 + j
    
# 방향화습약
cat5 = (categorydata[:,36] == 1)
cat5 = categorydata[cat5, 3:6]

ca5 = np.array([0,0,0])
for j in cat5:
    ca5 = ca5 + j

# 이수삼습약    
cat6 = (categorydata[:,37] == 1)
cat6 = categorydata[cat6, 3:6]

ca6 = np.array([0,0,0])
for j in cat6:
    ca6 = ca6 + j
    
# 온리약
cat7 = (categorydata[:,38] == 1)
cat7 = categorydata[cat7, 3:6]

ca7 = np.array([0,0,0])
for j in cat7:
    ca7 = ca7 + j

# 이기약    
cat8 = (categorydata[:,39] == 1)
cat8 = categorydata[cat8, 3:6]

ca8 = np.array([0,0,0])
for j in cat8:
    ca8 = ca8 + j

# 소식약
cat9 = (categorydata[:,40] == 1)
cat9 = categorydata[cat9, 3:6]

ca9 = np.array([0,0,0])
for j in cat9:
    ca9 = ca9 + j

# 구충약
cat10 = (categorydata[:,41] == 1)
cat10 = categorydata[cat10, 3:6]

ca10 = np.array([0,0,0])
for j in cat10:
    ca10 = ca10 + j

# 지혈약
cat11 = (categorydata[:,42] == 1)
cat11 = categorydata[cat11, 3:6]

ca11 = np.array([0,0,0])
for j in cat11:
    ca11 = ca11 + j

# 활혈거어약
cat12 = (categorydata[:,43] == 1)
cat12 = categorydata[cat12, 3:6]

ca12 = np.array([0,0,0])
for j in cat12:
    ca12 = ca12 + j

# 화담지해평천약
cat13 = (categorydata[:,44] == 1)
cat13 = categorydata[cat13, 3:6]

ca13 = np.array([0,0,0])
for j in cat13:
    ca13 = ca13 + j

# 안신약
cat14 = (categorydata[:,45] == 1)
cat14 = categorydata[cat14, 3:6]

ca14 = np.array([0,0,0])
for j in cat14:
    ca14 = ca14 + j

# 평간약
cat15 = (categorydata[:,46] == 1)
cat15 = categorydata[cat15, 3:6]

ca15 = np.array([0,0,0])
for j in cat15:
    ca15 = ca15 + j

# 개규약
cat16 = (categorydata[:,47] == 1)
cat16 = categorydata[cat16, 3:6]

ca16 = np.array([0,0,0])
for j in cat16:
    ca16 = ca16 + j

# 보익약
cat17 = (categorydata[:,48] == 1)
cat17 = categorydata[cat17, 3:6]

ca17 = np.array([0,0,0])
for j in cat17:
    ca17 = ca17 + j

# 수삽약
cat18 = (categorydata[:,49] == 1)
cat18 = categorydata[cat18, 3:6]

ca18 = np.array([0,0,0])
for j in cat18:
    ca18 = ca18 + j

# 용토약
cat19 = (categorydata[:,50] == 1)
cat19 = categorydata[cat19, 3:6]

ca19 = np.array([0,0,0])
for j in cat19:
    ca19 = ca19 + j

# 외용약
cat20 = (categorydata[:,51] == 1)
cat20 = categorydata[cat20, 3:6]

ca20 = np.array([0,0,0])
for j in cat20:
    ca20 = ca20 + j
    

category4 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca17, ca18, ca19, ca20]
category4 = np.array(category4)
category4 = category4[:,0:2]
category4 = np.transpose(category4)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number, rotation=90, fontsize = 15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category4, cmap=cmap)
plt.colorbar()

categoryexcel = category4[:,0:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jcjoint.xlsx')


category44 = [ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10, ca11, ca12, ca13, ca14, ca15, ca16, ca18, ca19, ca20]
category44 = np.array(category44)
category44 = category44[:,0:2]
category44 = np.transpose(category44)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)),number1, rotation=90, fontsize = 15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')
# heatmap 그래프 그리기
plt.imshow(category44, cmap=cmap)
plt.colorbar()

categoryexcel = category44[:,:]
categoryexcel = pd.DataFrame(categoryexcel)
categoryexcel.to_excel('category jcjoint without 17.xlsx')


category = np.concatenate((category1, category2, category3, category4))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*2,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)), number, fontsize=25)
plt.yticks(range(len(nation)), nation, fontsize=25)

cmap = plt.get_cmap('Reds')

plt.imshow(category, cmap=cmap)
plt.colorbar()



category = np.concatenate((category11, category22, category33, category44))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(number)*2,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(number)), number1, fontsize=25)
plt.yticks(range(len(nation)), nation, fontsize=25)
plt.legend(markerscale = 10)

cmap = plt.get_cmap('Reds')

plt.imshow(category, cmap=cmap)
plt.colorbar()


