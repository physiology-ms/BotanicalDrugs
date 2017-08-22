# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:31:03 2017

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

partdata = data.ix[:,1:78]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
part = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Radix', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')
part1 = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')

partdata = np.array(partdata)

# Animal Product 약물
APdata = (partdata[:,52] == 1)
APdata = partdata[APdata, 3:6]

ap = np.array([0,0,0])
for i in APdata:
    ap = ap + i

# Arillus 약물
aridata = (partdata[:,53] == 1)
aridata = partdata[aridata, 3:6]

ari = np.array([0,0,0])
for i in aridata:
    ari = ari + i
    
# Bulbus 약물
buldata = (partdata[:,54] == 1)
buldata = partdata[buldata, 3:6]

bul = np.array([0,0,0])
for i in buldata:
    bul = bul + i

# Calyx 약물
caldata = (partdata[:,55] == 1)
caldata = partdata[caldata, 3:6]

cal = np.array([0,0,0])
for i in caldata:
    cal = cal + i

# Caulis 약물
caudata = (partdata[:,56] == 1)
caudata = partdata[caudata, 3:6]

cau = np.array([0,0,0])
for i in caudata:
    cau = cau + i

# Cortex 약물
cordata = (partdata[:,57] == 1)
cordata = partdata[cordata, 3:6]

cor = np.array([0,0,0])
for i in cordata:
    cor = cor + i

# Essential oil 약물
oildata = (partdata[:,58] == 1)
oildata = partdata[oildata, 3:6]

oil = np.array([0,0,0])
for i in oildata:
    oil = oil + i

# Fermentata 약물
ferdata = (partdata[:,59] == 1)
ferdata = partdata[ferdata, 3:6]

fer = np.array([0,0,0])
for i in ferdata:
    fer = fer + i

# Flos 약물
flodata = (partdata[:,60] == 1)
flodata = partdata[flodata, 3:6]

flo = np.array([0,0,0])
for i in flodata:
    flo = flo + i
    
# Folium 약물
foldata = (partdata[:,61] == 1)
foldata = partdata[foldata, 3:6]

fol = np.array([0,0,0])
for i in foldata:
    fol = fol + i
    
# Fructus 약물
frudata = (partdata[:,62] == 1)
frudata = partdata[frudata, 3:6]

fru = np.array([0,0,0])
for i in frudata:
    fru = fru + i
    
# Herba 약물
herdata = (partdata[:,63] == 1)
herdata = partdata[herdata, 3:6]

her = np.array([0,0,0])
for i in herdata:
    her = her + i
    
# Lignum 약물
ligdata = (partdata[:,64] == 1)
ligdata = partdata[ligdata, 3:6]

lig = np.array([0,0,0])
for i in ligdata:
    lig = lig + i
    
# Medulla 약물
meddata = (partdata[:,65] == 1)
meddata = partdata[meddata, 3:6]

med = np.array([0,0,0])
for i in meddata:
    med = med + i
    
# Mineral product 약물
mpdata = (partdata[:,66] == 1)
mpdata = partdata[mpdata, 3:6]

mp = np.array([0,0,0])
for i in mpdata:
    mp = mp + i
    
# Pericarpium 약물
perdata = (partdata[:,67] == 1)
perdata = partdata[perdata, 3:6]

per = np.array([0,0,0])
for i in perdata:
    per = per + i
    
# Radix 약물
raddata = (partdata[:,68] == 1)
raddata = partdata[raddata, 3:6]

rad = np.array([0,0,0])
for i in raddata:
    rad = rad + i
    
# Ramulus 약물
ramdata = (partdata[:,69] == 1)
ramdata = partdata[ramdata, 3:6]

ram = np.array([0,0,0])
for i in ramdata:
    ram = ram + i
    
# Resin 약물
resdata = (partdata[:,70] == 1)
resdata = partdata[resdata, 3:6]

res = np.array([0,0,0])
for i in resdata:
    res = res + i
    
# Rhizoma 약물
rhidata = (partdata[:,71] == 1)
rhidata = partdata[rhidata, 3:6]

rhi = np.array([0,0,0])
for i in rhidata:
    rhi = rhi + i
    
# Sclerotium 약물
scldata = (partdata[:,72] == 1)
scldata = partdata[scldata, 3:6]

scl = np.array([0,0,0])
for i in scldata:
    scl = scl + i
    
# Semen 약물
semdata = (partdata[:,73] == 1)
semdata = partdata[semdata, 3:6]

sem = np.array([0,0,0])
for i in semdata:
    sem = sem + i
    
# spica 약물
spidata = (partdata[:,74] == 1)
spidata = partdata[spidata, 3:6]

spi = np.array([0,0,0])
for i in spidata:
    spi = spi + i
    
# Stigma 약물
stidata = (partdata[:,75] == 1)
stidata = partdata[stidata, 3:6]

sti = np.array([0,0,0])
for i in stidata:
    sti = sti + i
    
# Tuber 약물
tubdata = (partdata[:,76] == 1)
tubdata = partdata[tubdata, 3:6]

tub = np.array([0,0,0])
for i in tubdata:
    tub = tub + i


# 사기 통합 데이터(첫 행은 null파일)    
prtdata1 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, rad, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata1 = np.array(prtdata1)
prtdata1 = np.transpose(prtdata1)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata1, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata1[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part union.xlsx')


prtdata11 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata11 = np.array(prtdata11)
prtdata11 = np.transpose(prtdata11)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata11, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata11[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part union without radix.xlsx')


"""
"""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

partdata = data.ix[:,1:78]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
part = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Radix', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')
part1 = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')

partdata = np.array(partdata)

# Animal Product 약물
APdata = (partdata[:,52] == 1)
APdata = partdata[APdata, 3:6]

ap = np.array([0,0,0])
for i in APdata:
    ap = ap + i

# Arillus 약물
aridata = (partdata[:,53] == 1)
aridata = partdata[aridata, 3:6]

ari = np.array([0,0,0])
for i in aridata:
    ari = ari + i
    
# Bulbus 약물
buldata = (partdata[:,54] == 1)
buldata = partdata[buldata, 3:6]

bul = np.array([0,0,0])
for i in buldata:
    bul = bul + i

# Calyx 약물
caldata = (partdata[:,55] == 1)
caldata = partdata[caldata, 3:6]

cal = np.array([0,0,0])
for i in caldata:
    cal = cal + i

# Caulis 약물
caudata = (partdata[:,56] == 1)
caudata = partdata[caudata, 3:6]

cau = np.array([0,0,0])
for i in caudata:
    cau = cau + i

# Cortex 약물
cordata = (partdata[:,57] == 1)
cordata = partdata[cordata, 3:6]

cor = np.array([0,0,0])
for i in cordata:
    cor = cor + i

# Essential oil 약물
oildata = (partdata[:,58] == 1)
oildata = partdata[oildata, 3:6]

oil = np.array([0,0,0])
for i in oildata:
    oil = oil + i

# Fermentata 약물
ferdata = (partdata[:,59] == 1)
ferdata = partdata[ferdata, 3:6]

fer = np.array([0,0,0])
for i in ferdata:
    fer = fer + i

# Flos 약물
flodata = (partdata[:,60] == 1)
flodata = partdata[flodata, 3:6]

flo = np.array([0,0,0])
for i in flodata:
    flo = flo + i
    
# Folium 약물
foldata = (partdata[:,61] == 1)
foldata = partdata[foldata, 3:6]

fol = np.array([0,0,0])
for i in foldata:
    fol = fol + i
    
# Fructus 약물
frudata = (partdata[:,62] == 1)
frudata = partdata[frudata, 3:6]

fru = np.array([0,0,0])
for i in frudata:
    fru = fru + i
    
# Herba 약물
herdata = (partdata[:,63] == 1)
herdata = partdata[herdata, 3:6]

her = np.array([0,0,0])
for i in herdata:
    her = her + i
    
# Lignum 약물
ligdata = (partdata[:,64] == 1)
ligdata = partdata[ligdata, 3:6]

lig = np.array([0,0,0])
for i in ligdata:
    lig = lig + i
    
# Medulla 약물
meddata = (partdata[:,65] == 1)
meddata = partdata[meddata, 3:6]

med = np.array([0,0,0])
for i in meddata:
    med = med + i
    
# Mineral product 약물
mpdata = (partdata[:,66] == 1)
mpdata = partdata[mpdata, 3:6]

mp = np.array([0,0,0])
for i in mpdata:
    mp = mp + i
    
# Pericarpium 약물
perdata = (partdata[:,67] == 1)
perdata = partdata[perdata, 3:6]

per = np.array([0,0,0])
for i in perdata:
    per = per + i
    
# Radix 약물
raddata = (partdata[:,68] == 1)
raddata = partdata[raddata, 3:6]

rad = np.array([0,0,0])
for i in raddata:
    rad = rad + i
    
# Ramulus 약물
ramdata = (partdata[:,69] == 1)
ramdata = partdata[ramdata, 3:6]

ram = np.array([0,0,0])
for i in ramdata:
    ram = ram + i
    
# Resin 약물
resdata = (partdata[:,70] == 1)
resdata = partdata[resdata, 3:6]

res = np.array([0,0,0])
for i in resdata:
    res = res + i
    
# Rhizoma 약물
rhidata = (partdata[:,71] == 1)
rhidata = partdata[rhidata, 3:6]

rhi = np.array([0,0,0])
for i in rhidata:
    rhi = rhi + i
    
# Sclerotium 약물
scldata = (partdata[:,72] == 1)
scldata = partdata[scldata, 3:6]

scl = np.array([0,0,0])
for i in scldata:
    scl = scl + i
    
# Semen 약물
semdata = (partdata[:,73] == 1)
semdata = partdata[semdata, 3:6]

sem = np.array([0,0,0])
for i in semdata:
    sem = sem + i
    
# spica 약물
spidata = (partdata[:,74] == 1)
spidata = partdata[spidata, 3:6]

spi = np.array([0,0,0])
for i in spidata:
    spi = spi + i
    
# Stigma 약물
stidata = (partdata[:,75] == 1)
stidata = partdata[stidata, 3:6]

sti = np.array([0,0,0])
for i in stidata:
    sti = sti + i
    
# Tuber 약물
tubdata = (partdata[:,76] == 1)
tubdata = partdata[tubdata, 3:6]

tub = np.array([0,0,0])
for i in tubdata:
    tub = tub + i

prtdata2 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, rad, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata2 = np.array(prtdata2)
prtdata2 = np.transpose(prtdata2)

# 사기 통합 데이터(첫 행은 null파일)    
fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize = 0.15)

cmap = plt.get_cmap('Blues')

# heatmap 그래프 그리기
plt.imshow(prtdata2, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata2[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jkcjoint.xlsx')


prtdata22 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata22 = np.array(prtdata22)
prtdata22 = np.transpose(prtdata22)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*1,2))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(3), nation, fontsize = 0.15)

cmap = plt.get_cmap('Blues')

# heatmap 그래프 그리기
plt.imshow(prtdata22, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata22[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jkcjoint without radix.xlsx')


"""
"""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

partdata = data.ix[:,1:78]

namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')
part = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Radix', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')
part1 = ('NaN', 'AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')

partdata = np.array(partdata)

# Animal Product 약물
APdata = (partdata[:,52] == 1)
APdata = partdata[APdata, 3:6]

ap = np.array([0,0,0])
for i in APdata:
    ap = ap + i

# Arillus 약물
aridata = (partdata[:,53] == 1)
aridata = partdata[aridata, 3:6]

ari = np.array([0,0,0])
for i in aridata:
    ari = ari + i
    
# Bulbus 약물
buldata = (partdata[:,54] == 1)
buldata = partdata[buldata, 3:6]

bul = np.array([0,0,0])
for i in buldata:
    bul = bul + i

# Calyx 약물
caldata = (partdata[:,55] == 1)
caldata = partdata[caldata, 3:6]

cal = np.array([0,0,0])
for i in caldata:
    cal = cal + i

# Caulis 약물
caudata = (partdata[:,56] == 1)
caudata = partdata[caudata, 3:6]

cau = np.array([0,0,0])
for i in caudata:
    cau = cau + i

# Cortex 약물
cordata = (partdata[:,57] == 1)
cordata = partdata[cordata, 3:6]

cor = np.array([0,0,0])
for i in cordata:
    cor = cor + i

# Essential oil 약물
oildata = (partdata[:,58] == 1)
oildata = partdata[oildata, 3:6]

oil = np.array([0,0,0])
for i in oildata:
    oil = oil + i

# Fermentata 약물
ferdata = (partdata[:,59] == 1)
ferdata = partdata[ferdata, 3:6]

fer = np.array([0,0,0])
for i in ferdata:
    fer = fer + i

# Flos 약물
flodata = (partdata[:,60] == 1)
flodata = partdata[flodata, 3:6]

flo = np.array([0,0,0])
for i in flodata:
    flo = flo + i
    
# Folium 약물
foldata = (partdata[:,61] == 1)
foldata = partdata[foldata, 3:6]

fol = np.array([0,0,0])
for i in foldata:
    fol = fol + i
    
# Fructus 약물
frudata = (partdata[:,62] == 1)
frudata = partdata[frudata, 3:6]

fru = np.array([0,0,0])
for i in frudata:
    fru = fru + i
    
# Herba 약물
herdata = (partdata[:,63] == 1)
herdata = partdata[herdata, 3:6]

her = np.array([0,0,0])
for i in herdata:
    her = her + i
    
# Lignum 약물
ligdata = (partdata[:,64] == 1)
ligdata = partdata[ligdata, 3:6]

lig = np.array([0,0,0])
for i in ligdata:
    lig = lig + i
    
# Medulla 약물
meddata = (partdata[:,65] == 1)
meddata = partdata[meddata, 3:6]

med = np.array([0,0,0])
for i in meddata:
    med = med + i
    
# Mineral product 약물
mpdata = (partdata[:,66] == 1)
mpdata = partdata[mpdata, 3:6]

mp = np.array([0,0,0])
for i in mpdata:
    mp = mp + i
    
# Pericarpium 약물
perdata = (partdata[:,67] == 1)
perdata = partdata[perdata, 3:6]

per = np.array([0,0,0])
for i in perdata:
    per = per + i
    
# Radix 약물
raddata = (partdata[:,68] == 1)
raddata = partdata[raddata, 3:6]

rad = np.array([0,0,0])
for i in raddata:
    rad = rad + i
    
# Ramulus 약물
ramdata = (partdata[:,69] == 1)
ramdata = partdata[ramdata, 3:6]

ram = np.array([0,0,0])
for i in ramdata:
    ram = ram + i
    
# Resin 약물
resdata = (partdata[:,70] == 1)
resdata = partdata[resdata, 3:6]

res = np.array([0,0,0])
for i in resdata:
    res = res + i
    
# Rhizoma 약물
rhidata = (partdata[:,71] == 1)
rhidata = partdata[rhidata, 3:6]

rhi = np.array([0,0,0])
for i in rhidata:
    rhi = rhi + i
    
# Sclerotium 약물
scldata = (partdata[:,72] == 1)
scldata = partdata[scldata, 3:6]

scl = np.array([0,0,0])
for i in scldata:
    scl = scl + i
    
# Semen 약물
semdata = (partdata[:,73] == 1)
semdata = partdata[semdata, 3:6]

sem = np.array([0,0,0])
for i in semdata:
    sem = sem + i
    
# spica 약물
spidata = (partdata[:,74] == 1)
spidata = partdata[spidata, 3:6]

spi = np.array([0,0,0])
for i in spidata:
    spi = spi + i
    
# Stigma 약물
stidata = (partdata[:,75] == 1)
stidata = partdata[stidata, 3:6]

sti = np.array([0,0,0])
for i in stidata:
    sti = sti + i
    
# Tuber 약물
tubdata = (partdata[:,76] == 1)
tubdata = partdata[tubdata, 3:6]

tub = np.array([0,0,0])
for i in tubdata:
    tub = tub + i

    
# 사기 통합 데이터(첫 행은 null파일)    
prtdata3 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, rad, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata3 = np.array(prtdata3)
prtdata3 = prtdata3[:,0:2]
prtdata3 = np.transpose(prtdata3)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata3, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata3[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jkjoint.xlsx')


prtdata33 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata33 = np.array(prtdata33)
prtdata33 = prtdata33[:,0:2]
prtdata33 = np.transpose(prtdata33)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=0.15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata33, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata33[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jkjoint without radix.xlsx')


"""
"""



data = pd.read_excel('botanical data.xlsx', sheetname = 'japan china data')

#raw data 정리 및 파싱
#1행을 label로 인식하는 구조 때문에 null data = 0.0000001 추가
#왜인지는 모르겠지만 dataframe을 전체로 받아버리면 data 읽는 데 오류 > 구간으로 읽어야 숫자가 저장

partdata = data.ix[:,1:78]

namelist = data.ix[:,0]
nation = ('Japan', 'China', 'korea')
part = ('AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Radix', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')
part1 = ('AP', 'Arillus', 'Bulbus', 'Calyx', 'Caulis', 'Cortex', 'E_oil', 'Fermentata', 'Flos', 'Folium', 'Fructus', 'Herba', 'Lignum', 'Medulla', 'MP', 'Pericarpium', 'Ramulus', 'Resin', 'Rhizoma', 'Sclerotium', 'Semen', 'Spica', 'Stigma', 'Tuber')

partdata = np.array(partdata)

# Animal Product 약물
APdata = (partdata[:,52] == 1)
APdata = partdata[APdata, 3:6]

ap = np.array([0,0,0])
for i in APdata:
    ap = ap + i

# Arillus 약물
aridata = (partdata[:,53] == 1)
aridata = partdata[aridata, 3:6]

ari = np.array([0,0,0])
for i in aridata:
    ari = ari + i
    
# Bulbus 약물
buldata = (partdata[:,54] == 1)
buldata = partdata[buldata, 3:6]

bul = np.array([0,0,0])
for i in buldata:
    bul = bul + i

# Calyx 약물
caldata = (partdata[:,55] == 1)
caldata = partdata[caldata, 3:6]

cal = np.array([0,0,0])
for i in caldata:
    cal = cal + i

# Caulis 약물
caudata = (partdata[:,56] == 1)
caudata = partdata[caudata, 3:6]

cau = np.array([0,0,0])
for i in caudata:
    cau = cau + i

# Cortex 약물
cordata = (partdata[:,57] == 1)
cordata = partdata[cordata, 3:6]

cor = np.array([0,0,0])
for i in cordata:
    cor = cor + i

# Essential oil 약물
oildata = (partdata[:,58] == 1)
oildata = partdata[oildata, 3:6]

oil = np.array([0,0,0])
for i in oildata:
    oil = oil + i

# Fermentata 약물
ferdata = (partdata[:,59] == 1)
ferdata = partdata[ferdata, 3:6]

fer = np.array([0,0,0])
for i in ferdata:
    fer = fer + i

# Flos 약물
flodata = (partdata[:,60] == 1)
flodata = partdata[flodata, 3:6]

flo = np.array([0,0,0])
for i in flodata:
    flo = flo + i
    
# Folium 약물
foldata = (partdata[:,61] == 1)
foldata = partdata[foldata, 3:6]

fol = np.array([0,0,0])
for i in foldata:
    fol = fol + i
    
# Fructus 약물
frudata = (partdata[:,62] == 1)
frudata = partdata[frudata, 3:6]

fru = np.array([0,0,0])
for i in frudata:
    fru = fru + i
    
# Herba 약물
herdata = (partdata[:,63] == 1)
herdata = partdata[herdata, 3:6]

her = np.array([0,0,0])
for i in herdata:
    her = her + i
    
# Lignum 약물
ligdata = (partdata[:,64] == 1)
ligdata = partdata[ligdata, 3:6]

lig = np.array([0,0,0])
for i in ligdata:
    lig = lig + i
    
# Medulla 약물
meddata = (partdata[:,65] == 1)
meddata = partdata[meddata, 3:6]

med = np.array([0,0,0])
for i in meddata:
    med = med + i
    
# Mineral product 약물
mpdata = (partdata[:,66] == 1)
mpdata = partdata[mpdata, 3:6]

mp = np.array([0,0,0])
for i in mpdata:
    mp = mp + i
    
# Pericarpium 약물
perdata = (partdata[:,67] == 1)
perdata = partdata[perdata, 3:6]

per = np.array([0,0,0])
for i in perdata:
    per = per + i
    
# Radix 약물
raddata = (partdata[:,68] == 1)
raddata = partdata[raddata, 3:6]

rad = np.array([0,0,0])
for i in raddata:
    rad = rad + i
    
# Ramulus 약물
ramdata = (partdata[:,69] == 1)
ramdata = partdata[ramdata, 3:6]

ram = np.array([0,0,0])
for i in ramdata:
    ram = ram + i
    
# Resin 약물
resdata = (partdata[:,70] == 1)
resdata = partdata[resdata, 3:6]

res = np.array([0,0,0])
for i in resdata:
    res = res + i
    
# Rhizoma 약물
rhidata = (partdata[:,71] == 1)
rhidata = partdata[rhidata, 3:6]

rhi = np.array([0,0,0])
for i in rhidata:
    rhi = rhi + i
    
# Sclerotium 약물
scldata = (partdata[:,72] == 1)
scldata = partdata[scldata, 3:6]

scl = np.array([0,0,0])
for i in scldata:
    scl = scl + i
    
# Semen 약물
semdata = (partdata[:,73] == 1)
semdata = partdata[semdata, 3:6]

sem = np.array([0,0,0])
for i in semdata:
    sem = sem + i
    
# spica 약물
spidata = (partdata[:,74] == 1)
spidata = partdata[spidata, 3:6]

spi = np.array([0,0,0])
for i in spidata:
    spi = spi + i
    
# Stigma 약물
stidata = (partdata[:,75] == 1)
stidata = partdata[stidata, 3:6]

sti = np.array([0,0,0])
for i in stidata:
    sti = sti + i
    
# Tuber 약물
tubdata = (partdata[:,76] == 1)
tubdata = partdata[tubdata, 3:6]

tub = np.array([0,0,0])
for i in tubdata:
    tub = tub + i

    
# 사기 통합 데이터(첫 행은 null파일)    
prtdata4 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, rad, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata4 = np.array(prtdata4)
prtdata4 = prtdata4[:,0:2]
prtdata4 = np.transpose(prtdata4)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata4, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata4[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jcjoint.xlsx')


prtdata44 = [ap, ari, bul, cal, cau, cor, oil, fer, flo, fol, fru, her, lig, med, mp, per, ram, res, rhi, scl, sem, spi, sti, tub]
prtdata44 = np.array(prtdata44)
prtdata44 = prtdata44[:,0:2]
prtdata44 = np.transpose(prtdata44)

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,1))
# x축과 y축의 눈금개수
plt.xticks(range(len(part1)), part1, rotation=90, fontsize=15)
plt.yticks(range(2), nation, fontsize = 15)

cmap = plt.get_cmap('Reds')

# heatmap 그래프 그리기
plt.imshow(prtdata44, cmap=cmap)
plt.colorbar()

prtdataexcel = prtdata44[:,:]
prtdataexcel = pd.DataFrame(prtdataexcel)
prtdataexcel.to_excel('part jcjoint without radix.xlsx')




prtdata = np.concatenate((prtdata1, prtdata2, prtdata3, prtdata4))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part)*2,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(part)), part, rotation=90, fontsize=25)
plt.yticks(range(len(nation)), nation, fontsize=25)

cmap = plt.get_cmap('Reds')

plt.imshow(prtdata, cmap=cmap)
plt.colorbar()


prtdata = np.concatenate((prtdata11, prtdata22, prtdata33, prtdata44))
nation = ['japan','korea','china','japan','korea','china','japan','korea','japan','china']

fig = plt.figure()
# 그래프 사이즈
plt.figure(figsize=(len(part1)*2,10))
# x축과 y축의 눈금개수
plt.xticks(range(len(part1)), part1, rotation=90, fontsize=25)
plt.yticks(range(len(nation)), nation, fontsize=25)

cmap = plt.get_cmap('Reds')

plt.imshow(prtdata, cmap=cmap)
plt.colorbar()