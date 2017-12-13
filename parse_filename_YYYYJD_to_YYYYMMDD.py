# -*- coding: utf-8 -*-
############################################################################################################
"""
Created on Mon Sep 25 14:53:29 2017
@author: chinmay deval
#parses julian date from MODIS filenames (eg. MOD13Q1_NDVI_2000_049.tif) and saves date in YYYYMMDD format
to an excel sheet
"""
############################################################################################################

import os.path
import glob
import calendar
import pandas as pd



def JulianDate_to_MMDDYYY(y,jd):
    month = 1
    day = 0
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month = month + 1
    return month,jd,y

OutExcel= 'C:/Chinmay/mika_09_12_2017/analysis_output/dates.xlsx'
path_to_files= 'C:/Chinmay/mika_09_12_2017/data/MOD13V006/VI_16Days_250m_v6/NDVI/'

os.chdir(path_to_files)
filenames= sorted(glob.glob('*.tif'))

dates = []
for i in filenames:
    year= int((i[13:17]))
    Jday = int((i[18:21]))
#    print year, Jday
    dates.append(JulianDate_to_MMDDYYY(year, Jday))
datespd= pd.DataFrame(dates)
headers=['month','day','year']
datespd.to_excel(OutExcel, header = headers)  
