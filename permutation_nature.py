# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:16:44 2017

@author: physiology

본초 각각에서 한열온량평(사기)만 shuffling한 코드

결과 : 안좋음
 
"""

a='korea'
b='japan'
n=100000

import os
os.chdir(r'C:\Users\physiology\Desktop\paper')

    
def permutation_nation(n=None):

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
    import time
    
    time_start = time.time() #시간측정 시작
    if n == None:
        n = 100000
        
    a = input('nation? : ')
    b = input('another nation? : ')
    rawdata = pd.read_excel('botanical data.xlsx', sheetname = a + ' int resample') 
    rawdata2 = pd.read_excel('botanical data.xlsx', sheetname = b + ' int resample') 
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

    # data를 평균 + 비율화
    nationdata1 = np.sum(nationdata1, axis=0)/nationdata1.shape[0]
    nationdata1 = nationdata1/np.sum(nationdata1)
    
    nationdata2 = np.sum(nationdata2, axis=0)/nationdata2.shape[0]
    nationdata2 = nationdata2/np.sum(nationdata2)
    
    
    # positive set 점검용 positive real data 만드는 코드 추가
    testset1 = np.zeros((len(feature),1))
    testset2 = np.zeros((len(feature),1))
    
    for k in range(len(feature)):
        test1 = nationdata1[booleandata[k,:] == 1]
        test1 = np.sum(test1)
        testset1[k] = test1
        
        test2 = nationdata2[booleandata[k,:] == 1]
        test2 = np.sum(test2)
        testset2[k] = test2
    # positive real data        
    realdiff = abs(testset1-testset2)        



    ## permutation 코드 추가
    ## 약성(한열온량)만 섞음
    shuffle1 = np.zeros((len(feature), n))
    for i in range(n):
        shuf_nation = np.zeros((booleandata.shape[0], booleandata.shape[1]))
        for j in range(booleandata.shape[1]):
            shuf = np.random.permutation(booleandata[:,j])
            shuf_nation[:,j] = shuf
            
        for k in range(len(feature)):
        # if i=0, 한성의 약재가 true, 나머지가 false로 나뉨, 일련번호를 매기는 것
        # 앞에서 값이 true로 매겨진 순서의 본초 데이터만 모음. ex) 한성 약재 77개 > [3, 77, 50000] 행렬 생성
        # ex) booleandata = [true, false, false, true, true...] > 0번째, 3번째, 4번째.... 자료들만 모아서 array 생성
            data = nationdata1[shuf_nation[k,:] == 1]
            data = np.sum(data)
            shuffle1[k,i] = data
    
    
    shuffle2 = np.zeros((len(feature), n))
    for i in range(n):
        shuf_nation = np.zeros((booleandata.shape[0], booleandata.shape[1]))
        for j in range(booleandata.shape[1]):
            shuf = np.random.permutation(booleandata[:,j])
            shuf_nation[:,j] = shuf
        
        for k in range(len(feature)):
        # if i=0, 한성의 약재가 true, 나머지가 false로 나뉨, 일련번호를 매기는 것
        # 앞에서 값이 true로 매겨진 순서의 본초 데이터만 모음. ex) 한성 약재 77개 > [3, 77, 50000] 행렬 생성
        # ex) booleandata = [true, false, false, true, true...] > 0번째, 3번째, 4번째.... 자료들만 모아서 array 생성
            data = nationdata2[shuf_nation[k,:] == 1]
            data = np.sum(data)
            shuffle2[k,i] = data
            
    
    nullshuff = abs(shuffle1 - shuffle2)
    
    realdiff = abs(realdata[0,:]-realdata[1,:])
    realdiff = realdiff.reshape(69,1)
    
    nullshuffsort = np.sort(nullshuff)
    pval = nullshuffsort[:,95000]
    pval = pval.reshape(pval.shape[0],1)
    
    # 검정
    d = pval - realdiff
