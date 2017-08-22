# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
os.chdir(r'C:\Users\physiology\Desktop\paper')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/Malgun.ttf").get_name()
rc('font', family=font_name)

data = pd.read_excel('botanical data.xlsx', sheetname = 'mean data')

heatmapdata = data.ix[:,4:7]
namelist = data.ix[:,0]
nation = ('Japan', 'Korea', 'China')

heatmapdata = np.array(heatmapdata)
heatmapdata = np.transpose(heatmapdata)

namearray = np.arange(len(namelist))

fig = plt.figure()
plt.figure(figsize=(40,1.5))
plt.xticks(range(len(namelist)))
plt.yticks(range(3))
plt.xlim(1, len(namelist))

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
for label1 in ax.xaxis.get_ticklabels():
    label1.set_rotation(90)
#ax.yaxis.set_major_locator(tk.MultipleLocator())
#for label2 in ax.yaxis.get_ticklabels():
#    label2.set_rotation(45)
    
ax.xaxis.set_major_formatter(tk.FixedFormatter(namelist))
ax.yaxis.set_major_formatter(tk.FixedFormatter(nation))

cmap = plt.get_cmap('gist_heat_r')
#plt.hot()
plt.pcolormesh(heatmapdata, cmap=cmap)
plt.colorbar()
plt.savefig("heatmap union.png")

""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""

jointdata = pd.read_excel('botanical data.xlsx', sheetname = 'japan korea china data')

heatmapdata = jointdata.ix[:,4:7]
namelist = jointdata.ix[:,0]
nation = ('Japan', 'Korea', 'China')

heatmapdata = np.array(heatmapdata)
heatmapdata = np.transpose(heatmapdata)

namearray = np.arange(len(namelist))

fig = plt.figure()
plt.figure(figsize=(20,1.5))
plt.xticks(range(len(namelist)))
plt.yticks(range(3))
plt.xlim(1, len(namelist))

ax = plt.axes()
ax.xaxis.set_major_locator(tk.MultipleLocator())
for label1 in ax.xaxis.get_ticklabels():
    label1.set_rotation(90)
#ax.yaxis.set_major_locator(tk.MultipleLocator())
#for label2 in ax.yaxis.get_ticklabels():
#    label2.set_rotation(45)
    
ax.xaxis.set_major_formatter(tk.FixedFormatter(namelist))
ax.yaxis.set_major_formatter(tk.FixedFormatter(nation))

cmap = plt.get_cmap('gist_heat_r')
#plt.hot()
plt.pcolormesh(heatmapdata, cmap=cmap)
plt.colorbar()
plt.savefig("heatmap joint.png")