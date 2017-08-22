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
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자를 str으로 저장함

qidata = data.ix[:,1:14]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
fourqi = ('NaN', 'cold', 'cool', 'neutral', 'warm', 'hot')

qidata = np.array(qidata)

# 한성 약물
colddata = (qidata[:,8] == 1)
colddata = qidata[colddata, 3:6]

cold = np.array([0,0,0])
for i in colddata:
    cold = cold + i

# 량성 약물
cooldata = (qidata[:,9] == 1)
cooldata = qidata[cooldata, 3:6]

cool = np.array([0,0,0])
for i in cooldata:
    cool = cool + i
    
# 평성 약물
neutraldata = (qidata[:,10] == 1)
neutraldata = qidata[neutraldata, 3:6]

neutral = np.array([0,0,0])
for i in neutraldata:
    neutral = neutral + i

# 온성 약물
warmdata = (qidata[:,11] == 1)
warmdata = qidata[warmdata, 3:6]

warm = np.array([0,0,0])
for i in warmdata:
    warm = warm + i
    
# 열성 약물
hotdata = (qidata[:,12] == 1)
hotdata = qidata[hotdata, 3:6]

hot = np.array([0,0,0])
for i in hotdata:
    hot = hot + i

# 사기 통합 데이터(첫 행은 null파일)    
fourqidata1 = [cold, cool, neutral, warm, hot]
fourqidata1 = np.array(fourqidata1)
fourqidata1 = np.transpose(fourqidata1)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fourqi)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fourqi)),fourqi, rotation=90, fontsize = 0.1)
plt.yticks(range(3), nation, fontsize = 15)
# x축의 길이 : 
#plt.xlim(1, len(fourqi))

ax = plt.axes()
# x축의 눈금배치
ax.xaxis.set_major_locator(tk.MultipleLocator())
# x축 눈금이름 회전
#for label1 in ax.xaxis.get_ticklabels():
#    label1.set_rotation(90)

# x축과 y축 눈금이름 지정
#ax.xaxis.set_major_formatter(tk.FixedFormatter(fourqi))
#ax.yaxis.set_major_formatter(tk.FixedFormatter(nation))

# matplotlib에 저장되어 있는 색깔 불러오기
cmap = plt.get_cmap('Greens')
#plt.hot()

# heatmap 그래프 그리기
plt.imshow(fourqidata1, cmap=cmap)
#plt.pcolormesh(fourqidata, cmap=cmap)
plt.colorbar()

fourqidataexcel = fourqidata1[:,:]
fourqiexcel = pd.DataFrame(fourqidataexcel)
fourqiexcel.to_excel('fourqi union.xlsx')



"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자를 str으로 저장함

qidata = data.ix[:,1:14]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
fourqi = ('NaN', 'cold', 'cool', 'neutral', 'warm', 'hot')

qidata = np.array(qidata)

# 한성 약물
colddata = (qidata[:,8] == 1)
colddata = qidata[colddata, 3:6]

cold = np.array([0,0,0])
for i in colddata:
    cold = cold + i

# 량성 약물
cooldata = (qidata[:,9] == 1)
cooldata = qidata[cooldata, 3:6]

cool = np.array([0,0,0])
for i in cooldata:
    cool = cool + i
    
# 평성 약물
neutraldata = (qidata[:,10] == 1)
neutraldata = qidata[neutraldata, 3:6]

neutral = np.array([0,0,0])
for i in neutraldata:
    neutral = neutral + i

# 온성 약물
warmdata = (qidata[:,11] == 1)
warmdata = qidata[warmdata, 3:6]

warm = np.array([0,0,0])
for i in warmdata:
    warm = warm + i
    
# 열성 약물
hotdata = (qidata[:,12] == 1)
hotdata = qidata[hotdata, 3:6]

hot = np.array([0,0,0])
for i in hotdata:
    hot = hot + i

# 사기 통합 데이터(첫 행은 null파일)    
fourqidata2 = [cold, cool, neutral, warm, hot]
fourqidata2 = np.array(fourqidata2)
fourqidata2 = np.transpose(fourqidata2)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fourqi)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fourqi)),fourqi, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 0.15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Blues')

# heatmap 그래프 그리기
plt.imshow(fourqidata2, cmap=cmap)
plt.colorbar()

fourqidataexcel = fourqidata2[:,:]
fourqiexcel = pd.DataFrame(fourqidataexcel)
fourqiexcel.to_excel('fourqi jkcjoint.xlsx')



"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자를 str으로 저장함

qidata = data.ix[:,1:14]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea')
fourqi = ('NaN', 'cold', 'cool', 'neutral', 'warm', 'hot')

qidata = np.array(qidata)

# 한성 약물
colddata = (qidata[:,8] == 1)
colddata = qidata[colddata, 3:5]

cold = np.array([0,0])
for i in colddata:
    cold = cold + i

# 량성 약물
cooldata = (qidata[:,9] == 1)
cooldata = qidata[cooldata, 3:5]

cool = np.array([0,0])
for i in cooldata:
    cool = cool + i
    
# 평성 약물
neutraldata = (qidata[:,10] == 1)
neutraldata = qidata[neutraldata, 3:5]

neutral = np.array([0,0])
for i in neutraldata:
    neutral = neutral + i

# 온성 약물
warmdata = (qidata[:,11] == 1)
warmdata = qidata[warmdata, 3:5]

warm = np.array([0,0])
for i in warmdata:
    warm = warm + i
    
# 열성 약물
hotdata = (qidata[:,12] == 1)
hotdata = qidata[hotdata, 3:5]

hot = np.array([0,0])
for i in hotdata:
    hot = hot + i

# 사기 통합 데이터(첫 행은 null파일)    
fourqidata3 = [cold, cool, neutral, warm, hot]
fourqidata3 = np.array(fourqidata3)
fourqidata3 = np.transpose(fourqidata3)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fourqi)*0.8,1.6))
# x축과 y축의 눈금개수
plt.xticks(range(len(fourqi)),fourqi, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Greens')

# heatmap 그래프 그리기
plt.imshow(fourqidata3, cmap=cmap)
plt.colorbar()

fourqidataexcel = fourqidata3[:,:]
fourqiexcel = pd.DataFrame(fourqidataexcel)
fourqiexcel.to_excel('fourqi jkjoint.xlsx')




"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자를 str으로 저장함

qidata = data.ix[:,1:14]

namelist = data.ix[:,0]
nation = ('Japan', 'China')
fourqi = ('NaN', 'cold', 'cool', 'neutral', 'warm', 'hot')

qidata = np.array(qidata)

# 한성 약물
colddata = (qidata[:,8] == 1)
colddata = qidata[colddata, 3:5]

cold = np.array([0,0])
for i in colddata:
    cold = cold + i

# 량성 약물
cooldata = (qidata[:,9] == 1)
cooldata = qidata[cooldata, 3:5]

cool = np.array([0,0])
for i in cooldata:
    cool = cool + i
    
# 평성 약물
neutraldata = (qidata[:,10] == 1)
neutraldata = qidata[neutraldata, 3:5]

neutral = np.array([0,0])
for i in neutraldata:
    neutral = neutral + i

# 온성 약물
warmdata = (qidata[:,11] == 1)
warmdata = qidata[warmdata, 3:5]

warm = np.array([0,0])
for i in warmdata:
    warm = warm + i
    
# 열성 약물
hotdata = (qidata[:,12] == 1)
hotdata = qidata[hotdata, 3:5]

hot = np.array([0,0])
for i in hotdata:
    hot = hot + i

# 사기 통합 데이터(첫 행은 null파일)    
fourqidata4 = [cold, cool, neutral, warm, hot]
fourqidata4 = np.array(fourqidata4)
fourqidata4 = np.transpose(fourqidata4)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fourqi)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fourqi)),fourqi, rotation=90, fontsize = 15)
plt.yticks(range(3), nation, fontsize = 15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Greens')

# heatmap 그래프 그리기
plt.imshow(fourqidata4, cmap=cmap)
plt.colorbar()


fourqidataexcel = fourqidata4[:,:]
fourqiexcel = pd.DataFrame(fourqidataexcel)
fourqiexcel.to_excel('fourqi jcjoint.xlsx')



fourqidata = np.concatenate((fourqidata1, fourqidata2, fourqidata3, fourqidata4))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fourqi)*5,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(fourqi)),fourqi, rotation=90, fontsize = 20)
plt.yticks(range(len(nation)), nation, fontsize = 20)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Greens')

# heatmap 그래프 그리기
plt.imshow(fourqidata, cmap=cmap)
plt.colorbar()