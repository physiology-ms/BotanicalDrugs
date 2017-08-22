# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:49:07 2017

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
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

merdata = data.ix[:,1:33]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
mer = ('LU', 'LI', 'ST', 'SP', 'HT', 'SI', 'BL', 'KI', 'PC', 'TE', 'GB', 'LR')

merdata = np.array(merdata)

# 폐경 약물
ludata = (merdata[:,20] == 1)
ludata = merdata[ludata, 3:6]

lu = np.array([0,0,0])
for i in ludata:
    lu = lu + i

# 대장경 약물
lidata = (merdata[:,21] == 1)
lidata = merdata[lidata, 3:6]

li = np.array([0,0,0])
for i in lidata:
    li = li + i
    
# 위경 약물
stdata = (merdata[:,22] == 1)
stdata = merdata[stdata, 3:6]

st = np.array([0,0,0])
for i in stdata:
    st = st + i
    
# 비경 약물
spdata = (merdata[:,23] == 1)
spdata = merdata[spdata, 3:6]

sp = np.array([0,0,0])
for i in spdata:
    sp = sp + i

# 심경 약물
htdata = (merdata[:,24] == 1)
htdata = merdata[htdata,3:6]

ht = np.array([0,0,0])
for i in htdata:
    ht = ht + i
    
# 소장경 약물
sidata = (merdata[:,25] == 1)
sidata = merdata[sidata, 3:6]

si = np.array([0,0,0])
for i in sidata:
    si = si + i

# 방광경 약물
bldata = (merdata[:,26] == 1)
bldata = merdata[bldata, 3:6]

bl = np.array([0,0,0])
for i in bldata:
    bl = bl + i

# 신경 약물
kidata = (merdata[:,27] == 1)
kidata = merdata[kidata, 3:6]

ki = np.array([0,0,0])
for i in kidata:
    ki = ki + i

# 심포경 약물
pcdata = (merdata[:,28] == 1)
pcdata = merdata[pcdata, 3:6]

pc = np.array([0,0,0])
for i in pcdata:
    pc = pc + i

# 삼초경 약물
tedata = (merdata[:,29] == 1)
tedata = merdata[tedata, 3:6]

te = np.array([0,0,0])
for i in tedata:
    te = te + i

# 담경 약물
gbdata = (merdata[:,30] == 1)
gbdata = merdata[gbdata, 3:6]

gb = np.array([0,0,0])
for i in gbdata:
    gb = gb + i

# 간경 약물
lrdata = (merdata[:,31] == 1)
lrdata = merdata[lrdata, 3:6]

lr = np.array([0,0,0])
for i in lrdata:
    lr = lr + i  
    
# 사기 통합 데이터(첫 행은 null파일)    
medata1 = [lu, li, st, sp, ht, si, bl, ki, pc, te, gb, lr]
medata1 = np.array(medata1)
medata1 = np.transpose(medata1)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(mer)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(mer)), mer, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize=15)

cmap = plt.get_cmap('Reds')

plt.imshow(medata1, cmap=cmap)
plt.colorbar()

medataexcel = medata1[:,:]
meexcel = pd.DataFrame(medataexcel)
meexcel.to_excel('meridian union.xlsx')


"""""
"""""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

merdata = data.ix[:,1:33]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
mer = ('NaN', 'LU', 'LI', 'ST', 'SP', 'HT', 'SI', 'BL', 'KI', 'PC', 'TE', 'GB', 'LR')

merdata = np.array(merdata)

# 폐경 약물
ludata = (merdata[:,20] == 1)
ludata = merdata[ludata, 3:6]

lu = np.array([0,0,0])
for i in ludata:
    lu = lu + i

# 대장경 약물
lidata = (merdata[:,21] == 1)
lidata = merdata[lidata, 3:6]

li = np.array([0,0,0])
for i in lidata:
    li = li + i
    
# 위경 약물
stdata = (merdata[:,22] == 1)
stdata = merdata[stdata, 3:6]

st = np.array([0,0,0])
for i in stdata:
    st = st + i
    
# 비경 약물
spdata = (merdata[:,23] == 1)
spdata = merdata[spdata, 3:6]

sp = np.array([0,0,0])
for i in spdata:
    sp = sp + i

# 심경 약물
htdata = (merdata[:,24] == 1)
htdata = merdata[htdata,3:6]

ht = np.array([0,0,0])
for i in htdata:
    ht = ht + i
    
# 소장경 약물
sidata = (merdata[:,25] == 1)
sidata = merdata[sidata, 3:6]

si = np.array([0,0,0])
for i in sidata:
    si = si + i

# 방광경 약물
bldata = (merdata[:,26] == 1)
bldata = merdata[bldata, 3:6]

bl = np.array([0,0,0])
for i in bldata:
    bl = bl + i

# 신경 약물
kidata = (merdata[:,27] == 1)
kidata = merdata[kidata, 3:6]

ki = np.array([0,0,0])
for i in kidata:
    ki = ki + i

# 심포경 약물
pcdata = (merdata[:,28] == 1)
pcdata = merdata[pcdata, 3:6]

pc = np.array([0,0,0])
for i in pcdata:
    pc = pc + i

# 삼초경 약물
tedata = (merdata[:,29] == 1)
tedata = merdata[tedata, 3:6]

te = np.array([0,0,0])
for i in tedata:
    te = te + i

# 담경 약물
gbdata = (merdata[:,30] == 1)
gbdata = merdata[gbdata, 3:6]

gb = np.array([0,0,0])
for i in gbdata:
    gb = gb + i

# 간경 약물
lrdata = (merdata[:,31] == 1)
lrdata = merdata[lrdata, 3:6]

lr = np.array([0,0,0])
for i in lrdata:
    lr = lr + i  
   

# 사기 통합 데이터(첫 행은 null파일)    
medata2 = [lu, li, st, sp, ht, si, bl, ki, pc, te, gb, lr]
medata2 = np.array(medata2)
medata2 = np.transpose(medata2)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(mer)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(mer)), mer, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize=15)

cmap = plt.get_cmap('Reds')

plt.imshow(medata2, cmap=cmap)
plt.colorbar()

medataexcel = medata2[:,:]
meexcel = pd.DataFrame(medataexcel)
meexcel.to_excel('meridian jkcjoint.xlsx')


"""""
"""""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

merdata = data.ix[:,1:33]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea')
mer = ('NaN', 'LU', 'LI', 'ST', 'SP', 'HT', 'SI', 'BL', 'KI', 'PC', 'TE', 'GB', 'LR')

merdata = np.array(merdata)

# 폐경 약물
ludata = (merdata[:,20] == 1)
ludata = merdata[ludata, 3:5]

lu = np.array([0,0])
for i in ludata:
    lu = lu + i

# 대장경 약물
lidata = (merdata[:,21] == 1)
lidata = merdata[lidata, 3:5]

li = np.array([0,0])
for i in lidata:
    li = li + i
    
# 위경 약물
stdata = (merdata[:,22] == 1)
stdata = merdata[stdata, 3:5]

st = np.array([0,0])
for i in stdata:
    st = st + i
    
# 비경 약물
spdata = (merdata[:,23] == 1)
spdata = merdata[spdata, 3:5]

sp = np.array([0,0])
for i in spdata:
    sp = sp + i

# 심경 약물
htdata = (merdata[:,24] == 1)
htdata = merdata[htdata,3:5]

ht = np.array([0,0])
for i in htdata:
    ht = ht + i
    
# 소장경 약물
sidata = (merdata[:,25] == 1)
sidata = merdata[sidata, 3:5]

si = np.array([0,0])
for i in sidata:
    si = si + i

# 방광경 약물
bldata = (merdata[:,26] == 1)
bldata = merdata[bldata, 3:5]

bl = np.array([0,0])
for i in bldata:
    bl = bl + i

# 신경 약물
kidata = (merdata[:,27] == 1)
kidata = merdata[kidata, 3:5]

ki = np.array([0,0])
for i in kidata:
    ki = ki + i

# 심포경 약물
pcdata = (merdata[:,28] == 1)
pcdata = merdata[pcdata, 3:5]

pc = np.array([0,0])
for i in pcdata:
    pc = pc + i

# 삼초경 약물
tedata = (merdata[:,29] == 1)
tedata = merdata[tedata, 3:5]

te = np.array([0,0])
for i in tedata:
    te = te + i

# 담경 약물
gbdata = (merdata[:,30] == 1)
gbdata = merdata[gbdata, 3:5]

gb = np.array([0,0])
for i in gbdata:
    gb = gb + i

# 간경 약물
lrdata = (merdata[:,31] == 1)
lrdata = merdata[lrdata, 3:5]

lr = np.array([0,0])
for i in lrdata:
    lr = lr + i  
    
# 사기 통합 데이터(첫 행은 null파일)    
medata3 = [lu, li, st, sp, ht, si, bl, ki, pc, te, gb, lr]
medata3 = np.array(medata3)
medata3 = np.transpose(medata3)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(mer)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(mer)), mer, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize=15)

cmap = plt.get_cmap('Reds')

plt.imshow(medata3, cmap=cmap)
plt.colorbar()

medataexcel = medata3[:,:]
meexcel = pd.DataFrame(medataexcel)
meexcel.to_excel('meridian jkjoint.xlsx')

"""""
"""""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

merdata = data.ix[:,1:33]

namelist = data.ix[:,0]
nation = ('Japan', 'China')
mer = ('LU', 'LI', 'ST', 'SP', 'HT', 'SI', 'BL', 'KI', 'PC', 'TE', 'GB', 'LR')

merdata = np.array(merdata)

# 폐경 약물
ludata = (merdata[:,20] == 1)
ludata = merdata[ludata, 3:5]

lu = np.array([0,0])
for i in ludata:
    lu = lu + i

# 대장경 약물
lidata = (merdata[:,21] == 1)
lidata = merdata[lidata, 3:5]

li = np.array([0,0])
for i in lidata:
    li = li + i
    
# 위경 약물
stdata = (merdata[:,22] == 1)
stdata = merdata[stdata, 3:5]

st = np.array([0,0])
for i in stdata:
    st = st + i
    
# 비경 약물
spdata = (merdata[:,23] == 1)
spdata = merdata[spdata, 3:5]

sp = np.array([0,0])
for i in spdata:
    sp = sp + i

# 심경 약물
htdata = (merdata[:,24] == 1)
htdata = merdata[htdata,3:5]

ht = np.array([0,0])
for i in htdata:
    ht = ht + i
    
# 소장경 약물
sidata = (merdata[:,25] == 1)
sidata = merdata[sidata, 3:5]

si = np.array([0,0])
for i in sidata:
    si = si + i

# 방광경 약물
bldata = (merdata[:,26] == 1)
bldata = merdata[bldata, 3:5]

bl = np.array([0,0])
for i in bldata:
    bl = bl + i

# 신경 약물
kidata = (merdata[:,27] == 1)
kidata = merdata[kidata, 3:5]

ki = np.array([0,0])
for i in kidata:
    ki = ki + i

# 심포경 약물
pcdata = (merdata[:,28] == 1)
pcdata = merdata[pcdata, 3:5]

pc = np.array([0,0])
for i in pcdata:
    pc = pc + i

# 삼초경 약물
tedata = (merdata[:,29] == 1)
tedata = merdata[tedata, 3:5]

te = np.array([0,0])
for i in tedata:
    te = te + i

# 담경 약물
gbdata = (merdata[:,30] == 1)
gbdata = merdata[gbdata, 3:5]

gb = np.array([0,0])
for i in gbdata:
    gb = gb + i

# 간경 약물
lrdata = (merdata[:,31] == 1)
lrdata = merdata[lrdata, 3:5]

lr = np.array([0,0])
for i in lrdata:
    lr = lr + i  
    
# 사기 통합 데이터(첫 행은 null파일)    
medata4 = [lu, li, st, sp, ht, si, bl, ki, pc, te, gb, lr]
medata4 = np.array(medata4)
medata4 = np.transpose(medata4)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(mer)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(mer)), mer, rotation=90, fontsize=15)
plt.yticks(range(3), nation, fontsize=15)

cmap = plt.get_cmap('Reds')

plt.imshow(medata4, cmap=cmap)
plt.colorbar()

medataexcel = medata4[:,:]
meexcel = pd.DataFrame(medataexcel)
meexcel.to_excel('meridian jcjoint.xlsx')



medata = np.concatenate((medata1, medata2, medata3, medata4))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(mer)*2,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(mer)), mer, rotation=90, fontsize=15)
plt.yticks(range(len(nation)), nation, fontsize=15)

cmap = plt.get_cmap('Reds')

plt.imshow(medata, cmap=cmap)
plt.colorbar()