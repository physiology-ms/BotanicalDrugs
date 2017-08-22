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
#dataframe을 전체로 받아버리면 data 읽는 데 오류 > 행렬 안에 str 존재 때문인듯

flavdata = data.ix[:,1:21]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
fiveflav = ('NaN', 'sour','bitter','sweet','pungent','salty','astringent','tasteless')

flavdata = np.array(flavdata)

# 산 약물
sourdata = (flavdata[:,13] == 1)
sourdata = flavdata[sourdata, 3:6]

sour = np.array([0,0,0])
for i in sourdata:
    sour = sour + i

# 고 약물
bitterdata = (flavdata[:,14] == 1)
bitterdata = flavdata[bitterdata, 3:6]

bitter = np.array([0,0,0])
for i in bitterdata:
    bitter = bitter + i

# 감 약물
sweetdata = (flavdata[:,15] == 1)
sweetdata = flavdata[sweetdata, 3:6]

sweet = np.array([0,0,0])
for i in sweetdata:
    sweet = sweet + i

# 신 약물
pungentdata = (flavdata[:,16] == 1)
pungentdata = flavdata[pungentdata, 3:6]

pungent = np.array([0,0,0])
for i in pungentdata:
    pungent = pungent + i

# 함 약물
saltydata = (flavdata[:,17] == 1)
saltydata = flavdata[saltydata, 3:6]

salty = np.array([0,0,0])
for i in saltydata:
    salty = salty + i

# 삽 약물
astringentdata = (flavdata[:,18] == 1)
astringentdata = flavdata[astringentdata, 3:6]

astringent = np.array([0,0,0])
for i in astringentdata:
    astringent = astringent + i

# 담 약물
tastelessdata = (flavdata[:,19] == 1)
tastelessdata = flavdata[tastelessdata, 3:6]

tasteless = np.array([0,0,0])
for i in tastelessdata:
    tasteless = tasteless + i


# 사기 통합 데이터(첫 행은 null파일)   
 
fiveflavdata1 = [sour,bitter,sweet,pungent,salty,astringent,tasteless]
fiveflavdata1 = np.array(fiveflavdata1)
fiveflavdata1 = np.transpose(fiveflavdata1)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fiveflav)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fiveflav)), fiveflav, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(fiveflavdata1, cmap=cmap)
plt.colorbar()

fiveflavdataexcel = fiveflavdata1[:,:]
fiveflavdataexcel = pd.DataFrame(fiveflavdataexcel)
fiveflavdataexcel.to_excel('fiveflavor union.xlsx')

"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#dataframe을 전체로 받아버리면 data 읽는 데 오류 > 행렬 안에 str 존재 때문인듯

flavdata = data.ix[:,1:21]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
fiveflav = ('NaN', 'sour','bitter','sweet','pungent','salty','astringent','tasteless')

flavdata = np.array(flavdata)

# 산 약물
sourdata = (flavdata[:,13] == 1)
sourdata = flavdata[sourdata, 3:6]

sour = np.array([0,0,0])
for i in sourdata:
    sour = sour + i

# 고 약물
bitterdata = (flavdata[:,14] == 1)
bitterdata = flavdata[bitterdata, 3:6]

bitter = np.array([0,0,0])
for i in bitterdata:
    bitter = bitter + i

# 감 약물
sweetdata = (flavdata[:,15] == 1)
sweetdata = flavdata[sweetdata, 3:6]

sweet = np.array([0,0,0])
for i in sweetdata:
    sweet = sweet + i

# 신 약물
pungentdata = (flavdata[:,16] == 1)
pungentdata = flavdata[pungentdata, 3:6]

pungent = np.array([0,0,0])
for i in pungentdata:
    pungent = pungent + i

# 함 약물
saltydata = (flavdata[:,17] == 1)
saltydata = flavdata[saltydata, 3:6]

salty = np.array([0,0,0])
for i in saltydata:
    salty = salty + i

# 삽 약물
astringentdata = (flavdata[:,18] == 1)
astringentdata = flavdata[astringentdata, 3:6]

astringent = np.array([0,0,0])
for i in astringentdata:
    astringent = astringent + i

# 담 약물
tastelessdata = (flavdata[:,19] == 1)
tastelessdata = flavdata[tastelessdata, 3:6]

tasteless = np.array([0,0,0])
for i in tastelessdata:
    tasteless = tasteless + i


# 사기 통합 데이터(첫 행은 null파일)    
fiveflavdata2 = [sour,bitter,sweet,pungent,salty,astringent,tasteless]
fiveflavdata2 = np.array(fiveflavdata2)
fiveflavdata2 = np.transpose(fiveflavdata2)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fiveflav)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fiveflav)), fiveflav, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 0.15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Blues')

# heatmap 그래프 그리기
plt.imshow(fiveflavdata2, cmap=cmap)
plt.colorbar()


fiveflavdataexcel = fiveflavdata2[:,:]
fiveflavdataexcel = pd.DataFrame(fiveflavdataexcel)
fiveflavdataexcel.to_excel('fiveflavor jkcjoint.xlsx')

"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#dataframe을 전체로 받아버리면 data 읽는 데 오류 > 행렬 안에 str 존재 때문인듯

flavdata = data.ix[:,1:21]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea')
fiveflav = ('NaN', 'sour','bitter','sweet','pungent','salty','astringent','tasteless')

flavdata = np.array(flavdata)

# 산 약물
sourdata = (flavdata[:,13] == 1)
sourdata = flavdata[sourdata, 3:5]

sour = np.array([0,0])
for i in sourdata:
    sour = sour + i

# 고 약물
bitterdata = (flavdata[:,14] == 1)
bitterdata = flavdata[bitterdata, 3:5]

bitter = np.array([0,0])
for i in bitterdata:
    bitter = bitter + i

# 감 약물
sweetdata = (flavdata[:,15] == 1)
sweetdata = flavdata[sweetdata, 3:5]

sweet = np.array([0,0])
for i in sweetdata:
    sweet = sweet + i

# 신 약물
pungentdata = (flavdata[:,16] == 1)
pungentdata = flavdata[pungentdata, 3:5]

pungent = np.array([0,0])
for i in pungentdata:
    pungent = pungent + i

# 함 약물
saltydata = (flavdata[:,17] == 1)
saltydata = flavdata[saltydata, 3:5]

salty = np.array([0,0])
for i in saltydata:
    salty = salty + i

# 삽 약물
astringentdata = (flavdata[:,18] == 1)
astringentdata = flavdata[astringentdata, 3:5]

astringent = np.array([0,0])
for i in astringentdata:
    astringent = astringent + i

# 담 약물
tastelessdata = (flavdata[:,19] == 1)
tastelessdata = flavdata[tastelessdata, 3:5]

tasteless = np.array([0,0])
for i in tastelessdata:
    tasteless = tasteless + i


# 사기 통합 데이터(첫 행은 null파일)    
fiveflavdata3 = [sour,bitter,sweet,pungent,salty,astringent,tasteless]
fiveflavdata3 = np.array(fiveflavdata3)
fiveflavdata3 = np.transpose(fiveflavdata3)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fiveflav)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fiveflav)), fiveflav, rotation=90, fontsize = 0.15)
plt.yticks(range(3), nation, fontsize = 15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(fiveflavdata3, cmap=cmap)
plt.colorbar()

fiveflavdataexcel = fiveflavdata3[:,:]
fiveflavdataexcel = pd.DataFrame(fiveflavdataexcel)
fiveflavdataexcel.to_excel('fiveflavor jkjoint.xlsx')

"""""
"""""


data = pd.read_excel('botanical data.xlsx', sheetname = 'japan china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#dataframe을 전체로 받아버리면 data 읽는 데 오류 > 행렬 안에 str 존재 때문인듯

flavdata = data.ix[:,1:21]

namelist = data.ix[:,0]
nation = ('Japan', 'China')
fiveflav = ('NaN', 'sour','bitter','sweet','pungent','salty','astringent','tasteless')

flavdata = np.array(flavdata)

# 산 약물
sourdata = (flavdata[:,13] == 1)
sourdata = flavdata[sourdata, 3:5]

sour = np.array([0,0])
for i in sourdata:
    sour = sour + i

# 고 약물
bitterdata = (flavdata[:,14] == 1)
bitterdata = flavdata[bitterdata, 3:5]

bitter = np.array([0,0])
for i in bitterdata:
    bitter = bitter + i

# 감 약물
sweetdata = (flavdata[:,15] == 1)
sweetdata = flavdata[sweetdata, 3:5]

sweet = np.array([0,0])
for i in sweetdata:
    sweet = sweet + i

# 신 약물
pungentdata = (flavdata[:,16] == 1)
pungentdata = flavdata[pungentdata, 3:5]

pungent = np.array([0,0])
for i in pungentdata:
    pungent = pungent + i

# 함 약물
saltydata = (flavdata[:,17] == 1)
saltydata = flavdata[saltydata, 3:5]

salty = np.array([0,0])
for i in saltydata:
    salty = salty + i

# 삽 약물
astringentdata = (flavdata[:,18] == 1)
astringentdata = flavdata[astringentdata, 3:5]

astringent = np.array([0,0])
for i in astringentdata:
    astringent = astringent + i

# 담 약물
tastelessdata = (flavdata[:,19] == 1)
tastelessdata = flavdata[tastelessdata, 3:5]

tasteless = np.array([0,0])
for i in tastelessdata:
    tasteless = tasteless + i


# 사기 통합 데이터(첫 행은 null파일)    
fiveflavdata4 = [sour,bitter,sweet,pungent,salty,astringent,tasteless]
fiveflavdata4 = np.array(fiveflavdata4)
fiveflavdata4 = np.transpose(fiveflavdata4)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fiveflav)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(fiveflav)), fiveflav, rotation=90, fontsize = 15)
plt.yticks(range(3), nation, fontsize = 15)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(fiveflavdata4, cmap=cmap)
plt.colorbar()

fiveflavdataexcel = fiveflavdata4[:,:]
fiveflavdataexcel = pd.DataFrame(fiveflavdataexcel)
fiveflavdataexcel.to_excel('fiveflavor jcjoint.xlsx')


fiveflavdata = np.concatenate((fiveflavdata1, fiveflavdata2, fiveflavdata3, fiveflavdata4))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(fiveflav)*5,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(fiveflav)), fiveflav, rotation=90, fontsize = 20)
plt.yticks(range(len(nation)), nation, fontsize = 20)

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(fiveflavdata, cmap=cmap)
plt.colorbar()
