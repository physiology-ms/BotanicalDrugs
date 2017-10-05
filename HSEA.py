# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:45:05 2017

@author: physiology

본초를 매개로 Herb set enrichment analysis 만드는 코드

조정변수 : a, b, rawdata, feature number

10.03 : permutation 추가
n = permution 횟수
그림에 pvalue 추가

10.05 : p-value 0.05 이하만 그림으로 저장

"""
## a,b는 비교국가
a='korea'
b='japan'
## n = permutition 횟수 
n=1000


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



corrdata = np.concatenate((np.array(nationdata1, ndmin=2).T,np.array(nationdata2, ndmin=2).T), axis=1)
nulldata = np.zeros((corrdata.shape[0], corrdata.shape[1]))
nulldata[:,0] = 1




nationdata = nationdata1 - nationdata2
nationdata = pd.DataFrame(nationdata)
nationdata.columns = ['diff']
dfbooleandata = pd.DataFrame(booleandata)
nationdata = pd.concat((rawdata['name'],nationdata,dfbooleandata), axis=1)
nationdata = nationdata.sort_values(by='diff', ascending=False)

tickerdata = nationdata.reset_index()
#nationdata = np.concatenate((nationdata1, nationdata2))
#for i in range(nationdata2.shape[0]-1):
#    nationdata = np.concatenate((nationdata, nationdata1))
#for i in range(nationdata1.shape[0]-1):
#    nationdata = np.concatenate((nationdata, nationdata2))

class _MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
    
norm = _MidpointNormalize(midpoint=0)


"""
10.05 p-val 0.05 이하만 그림으로 저장
"""

for ii in range(len(feature)):
    os.chdir(r'C:\Users\physiology\Desktop\paper')
    ## feature_num = visualize할 feature number
    feature_num = ii

    ## x축 index
    x = tickerdata.index.values

    ## diff가 0에 가까운 값 찾기(기준선, 중심선)
    zeroscore = 1
    zeroenu = 0
    zerotest = list(abs(tickerdata['diff']))
    for i, element in enumerate(zerotest):
        if zeroscore > element:
            zeroscore = element
            zeroenu = i
            
    ## heatmap에 들어갈 데이터 정리
    im_matrix = np.array(tickerdata['diff'])
    im_matrix = np.reshape(im_matrix,(1,im_matrix.shape[0]))
    
    ## 바코드 모양 feature set에 들어갈 본초 모음
    ax3list = []
    for i,element in enumerate(tickerdata[feature_num]):
        if element == 1:
            ax3list.append(i)


    ## Ranked estimate score 구하는 과정
    tag_indicator = np.array(tickerdata[feature_num])
    N = len(tickerdata)
    Nhit = np.sum(tag_indicator)
    
    # 해당되는 feature가 하나도 없으면 error. error 방지
    if Nhit == 0:
        continue
    
    correl_vector = np.abs(tickerdata['diff'])
    sum_correl_tag = np.sum(correl_vector[tag_indicator.astype(bool)])
    
    no_tag_indicator = 1 - tag_indicator
    Nmiss =  N - Nhit 
    norm_tag =  1.0/sum_correl_tag
    norm_no_tag = 1.0/Nmiss
           
    RES = np.cumsum(tag_indicator * correl_vector * norm_tag - no_tag_indicator * norm_no_tag)      
    max_ES = np.max(RES)
    min_ES = np.min(RES)
        
    es = np.where(np.abs(max_ES) > np.abs(min_ES), max_ES, min_ES)


 
    """
    10.03 permutation

    es 수정 : permutation 단계에서 es가 음수로 나오는 경우가 존재

    가장 큰 값을 골라내기 위해 abs를 제거

    """
    pval_list = []
    for i in range(n):
        tag_indicator_per = np.random.permutation(tag_indicator)
        
        sum_correl_tag_per = np.sum(correl_vector[tag_indicator_per.astype(bool)])
    
        no_tag_indicator_per = 1 - tag_indicator_per
        norm_tag_per =  1.0/sum_correl_tag_per
        norm_no_tag_per = 1.0/Nmiss
        
        RES_per = np.cumsum(tag_indicator_per * correl_vector * norm_tag_per - no_tag_indicator_per * norm_no_tag_per)      
        max_ES_per = np.max(RES_per)
        min_ES_per = np.min(RES_per)
        
        es_per = np.where(max_ES_per > min_ES_per, max_ES_per, min_ES_per)
        
        pval_list.append(es_per)
        
    pval = np.sum(es < pval_list)/n
    
    # p-value 필터 설정
    if pval <= 0.05:
        ## figure        

        figsize = (6,6)
        gs = plt.GridSpec(16,1)
        fig = plt.figure(figsize=figsize)
        canvas = FigureCanvas(fig)


        # Correlation
        ax1 =  fig.add_subplot(gs[11:])
        ax1.fill_between(x, y1= tickerdata['diff'], y2=0, color='grey')
        ax1.set_ylabel("Ranked difference", fontsize=14)    
        ax1.text(.05, .9, 'Positively Correlated', color='red', horizontalalignment='left', verticalalignment='top',\
         transform=ax1.transAxes)
        ax1.text(.95, .05, 'Negatively Correlated', color='Blue', horizontalalignment='right', verticalalignment='bottom',\
         transform=ax1.transAxes)

        trans1 = transforms.blended_transform_factory(ax1.transData, ax1.transAxes)

        # vlines와 text의 첫 번째 요소는 corr=0이 되는 점
        # 가운데 점선
        ax1.vlines(zeroenu, -0.05, 0.05, linewidth=1, linestyles='--', color='grey')
        # 가운데 number
        ax1.text(zeroenu, 0.5, 'zeroscore at '+str(zeroenu), horizontalalignment='center', verticalalignment='center', transform=trans1)    
        ax1.set_xlabel("Rank in Ordered Dataset", fontsize=14)
        
        #ax1.spines['top'].set_visible(False)
        ax1.tick_params(axis='both', which='both', top='off', right='off', left='off')
        ax1.locator_params(axis='y', nbins=5)
        ax1.locator_params(axis='x', nbins=5)    
        #ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda tick_loc,tick_num :  '{:.1f}'.format(tick_loc) ))
        
        
        # Correlation colormap
        ax2 =  fig.add_subplot(gs[10], sharex=ax1)
        
        # 맨앞의 숫자는 rank matrix
        ax2.imshow(im_matrix, aspect='auto', norm = norm, cmap=plt.cm.seismic, interpolation='none')
        #ax2.imshow(im_matrix, aspect='auto', cmap=plt.cm.seismic, interpolation='none') # cm.coolwarm
        #ax2.spines['bottom'].set_visible(False)
        ax2.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off',labelleft='off')
        
        
        
        # botanical hits
        ax3 = fig.add_subplot(gs[8:10], sharex=ax1)
        trans3 = transforms.blended_transform_factory(ax3.transData, ax3.transAxes)
        # 맨 앞의 숫자는 hit하는 본초
        ax3.vlines(ax3list, 0, 1,linewidth=.5,transform=trans3)
        #ax3.spines['bottom'].set_visible(False)
        ax3.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
        
        # Enrichment score
        ax4 = fig.add_subplot(gs[:8], sharex=ax1)
        # x,y는 차원값
        # x는 rank의 index, y는 enrichment score
        ax4.plot(x, RES, linewidth=4, color ='#88C544')
        
        ##ES
        ax4.text(.1, .1, 'ES: '+str(max_ES), transform=ax4.transAxes)
        ##fdr
        #ax4.text(.1, .1, 0.036, transform=ax4.transAxes)
        ##pval
        ax4.text(.1, .2, 'P-value: '+"{:.3f}".format(float(pval)), transform=ax4.transAxes)
        ##nes
        #ax4.text(.1, .3, -1.603, transform=ax4.transAxes)
        
        # the y coords of this transformation are data, and the x coord are axes
        trans4 = transforms.blended_transform_factory(ax4.transAxes, ax4.transData)
        ax4.hlines(0, 0, 1, linewidth=.5, transform=trans4, color='grey')
        ax4.set_ylabel("Enrichment score (ES)", fontsize=14)
        #ax4.set_xlim(min(x), max(x))
        ax4.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off')
        ax4.locator_params(axis='y', nbins=5)
        # FuncFormatter need two argment, I don't know why. this lambda function used to format yaxis tick labels.
        ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda tick_loc,tick_num :  '{:.1f}'.format(tick_loc)))
        fig.suptitle(feature[feature_num], fontsize=16)
        fig.subplots_adjust(hspace=0)
        
        os.chdir(r"./HSEA")
        plt.savefig("HSEA_"+a+"_"+b+"_"+feature[ii]+".png")
    
    else:
        continue
