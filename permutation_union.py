# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:25:47 2017

@author: physiology

한-중-일 나라끼리 섞어 permutation하는 코드

"""
import os
os.chdir(r'C:\Users\physiology\Desktop\paper')

def permutation(n=None):
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
    import time
    
    time_start = time.time() #시간측정 시작
    if n == None:
        n = 50000
    
    a = input('nation? : ')
    b = input('another nation? : ')
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
        
    booleandata = rawdata.ix[:,11:16]
    
    feature = booleandata.columns
    # column 이름을 튜플 구조로 저장
    feature = tuple(feature)
    
    nationdata1 = np.array(nationdata1)
    nationdata1 = np.transpose(nationdata1) # (일본 기준) 7 * 본초 수

    nationdata2 = np.array(nationdata2)
    nationdata2 = np.transpose(nationdata2)
    
    booleandata = np.array(booleandata) # 본초수 * 69
    booleandata = np.transpose(booleandata) # 69feature * 본초수
    
    realdata = realdata.ix[:,1:]
    realdata = np.array(realdata)
    
    nationdata = np.concatenate((nationdata1, nationdata2)) # 한국 = 일본 같은 개수 만들기 위헤
    for i in range(nationdata2.shape[0]-1):
        nationdata = np.concatenate((nationdata, nationdata1))
    for i in range(nationdata1.shape[0]-1):
        nationdata = np.concatenate((nationdata, nationdata2))
    
        
    
     #동일한 사이즈의 영행렬을 n개 생성
    shuffle2 = np.zeros((nationdata.shape[0], booleandata.shape[0], n)) # 42 * 69 * 50000
    
    for i in range(n):
        shuffle = np.zeros((nationdata.shape[0], nationdata.shape[1]))
        
        for j in range(nationdata.shape[1]):
            shuffle[:, j] = np.random.permutation(nationdata[:,j])
        
        # shuffle을 비율화
        shuffle = shuffle/np.reshape(np.sum(shuffle, axis=1),(nationdata.shape[0],1))
        
        for k in range(len(feature)):
        # if i=0, 한성의 약재가 true, 나머지가 false로 나뉨, 일련번호를 매기는 것
            data = (booleandata[k,:] == 1)
        # 앞에서 값이 true로 매겨진 순서의 본초 데이터만 모음. ex) 한성 약재 77개 > [3, 77, 50000] 행렬 생성
        # ex) booleandata = [true, false, false, true, true...] > 0번째, 3번째, 4번째.... 자료들만 모아서 array 생성
            dataset = shuffle[:,data]

            dataset = np.sum(dataset, axis = 1)
            shuffle2[:,k,i] = dataset
                    
    nullshuff1 = abs(shuffle2[0] - shuffle2[1])    
    nullshuff2 = abs(shuffle2[2] - shuffle2[3])
    nullshuff = np.concatenate((nullshuff1, nullshuff2), axis = 1)
    
    
    realdiff = abs(realdata[0,:]-realdata[1,:])
    realdiff = realdiff.reshape(69,1)
    
    nullshuff = np.sort(nullshuff)
    pval = nullshuff[:,95000]
    pval = pval.reshape(69,1)
    
    per = np.concatenate((realdiff, pval), axis = 1)
    per = pd.DataFrame(per)
    per.to_excel(a + b +' permutation union.xlsx')

