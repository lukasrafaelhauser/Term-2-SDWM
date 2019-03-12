#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:25:08 2019

@author: l-r-h
"""

#%%

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.base import BaseEstimator
from sklearn.neighbors import LocalOutlierFactor
from sklearn.feature_selection import VarianceThreshold

from sklearn.pipeline import Pipeline

from sklearn import linear_model
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import KFold

from sklearn.metrics import mean_squared_error

from sklearn.pipeline import make_pipeline

import datetime as dt

#%%

jan = pd.ExcelFile('/Users/l-r-h/Desktop/IE/Term_2/Term Integration Project/ENE - 02.- MONTHLY INCIDENTS Real Time (1).xlsx', sep=',')
feb = pd.ExcelFile('/Users/l-r-h/Desktop/IE/Term_2/Term Integration Project/FEB - 02.- MONTHLY INCIDENTS Real Time.xlsx', sep=',')
janjun = pd.ExcelFile('/Users/l-r-h/Desktop/IE/Term_2/Term Integration Project/Incidents by service and applications JAN-JUN2018.xls', sep=',')
criser = pd.ExcelFile('/Users/l-r-h/Desktop/IE/Term_2/Term Integration Project/20190125 Critical services - application.xls', sep=',')

#%%

dfs = {sheet_name: jan.parse(sheet_name) 
          for sheet_name in jan.sheet_names}

jan_mir = dfs.get('MONTHLY INCIDENTS RAISED')
jan_mir1 = jan_mir.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], axis= 0)
jan_mir1.reset_index()

#%%

dfs2 = {sheet_name: feb.parse(sheet_name) 
          for sheet_name in feb.sheet_names}

febm = dfs2.get('MONTHLY INCIDENTS RAISED')
febm = febm.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], axis= 0)
febm.reset_index()

febm.columns = febm.iloc[0]
febm = febm.reset_index()
febm = febm.drop(16)

jan_mir1.columns = jan_mir1.iloc[0]
jan_mir1.reset_index()
jan_mir1 = jan_mir1.drop(17)
#%%

dfs3 = {sheet_name: janjun.parse(sheet_name) 
          for sheet_name in janjun.sheet_names}

janjundata = dfs3.get('Data')
#%%
all_mir = pd.concat([jan_mir1, febm])
all_mir.rename(columns={'Incidenct Code': 'Incident ID'}, inplace=True)


all_mir2 = pd.merge(all_mir, janjundata, how='inner', on=['Incident ID'])
#%%

dfs4 = {sheet_name: criser.parse(sheet_name) 
          for sheet_name in criser.sheet_names}

criser2 = dfs4.get('Dominio-ser-aplic')
criser2 = criser2.drop(0)
criser2.columns = criser2.iloc[0]
criser2 = criser2.drop(1)
criser2.rename(columns={'Application': 'CI Name'}, inplace=True)



#%%
a= []
def filter_data(prio, stat=['Resolved', 'Pending']):
    request = all_mir3[all_mir3.Priority_x.isin(prio) & all_mir3.incstatus.isin(stat)]
    a.append(request)
    return a
    


#%%
#jan_mir1_cri = jan_mir1.loc[jan_mir1['Priority'] == 'Crítica']
#jmc = jan_mir1_cri
#

all_mir2['Create Date-Time'] = pd.to_datetime(all_mir2['Create Date-Time'], dayfirst=True)
all_mir2['Resolution Date-Time'] = pd.to_datetime(all_mir2['Resolution Date-Time'], dayfirst=True)
all_mir2['Res-time'] = all_mir2['Resolution Date-Time'] - all_mir2['Create Date-Time']
#jmc['Hour Create'] = pd.DatetimeIndex(jmc['Create Date-Time']).hour


#%%
#jan_mir1_cri['Incidenct Code'].astype(str)
#jan_mir1_cri['Create Date-Time'].astype(str)
#
#jan_mir1_cri['Year'] = pd.DatetimeIndex(jan_mir1_cri['Create Date-Time']).year
#jan_mir1_cri['Month'] = pd.DatetimeIndex(jan_mir1_cri['Create Date-Time']).day
#jan_mir1_cri['Day'] = pd.DatetimeIndex(jan_mir1_cri['Create Date-Time']).month
#
#jan_mir1_cri['Day'].astype(int)
#jan_mir1_cri[['Day', 'Incidenct Code']].groupby('Day').agg(sum).plot()
#
#jan_mir1_cri[['Day', 'Incidenct Code']].groupby(['Day'])['Incidenct Code'].nunique().agg(sum).plot()
#
all_mir3 = pd.merge(all_mir2, criser2, how='inner', on=['CI Name'])
all_mir3.rename(columns={'Incident Status': 'incstatus'}, inplace=True)
all_mir3.rename(columns={'Incident ID': 'inc_id'}, inplace=True)
#%%

all_mir3['Create Date-Time'] = pd.to_datetime(all_mir3['Create Date-Time'], dayfirst=True)
all_mir3['Res-time'] = all_mir3['Resolution Date-Time'] - all_mir3['Create Date-Time']
all_mir3['date_create'] = pd.DatetimeIndex(all_mir3['Create Date-Time']).date
all_mir4= all_mir3[['Create Date-Time','inc_id']].groupby(['Create Date-Time']).nunique()
#dt.datetime.combine(all_mir4.index, datetime.time())
all_mir5= all_mir3[['Service','inc_id']].groupby(['Service']).nunique()
all_mir6= all_mir3[all_mir3.Priority_x.isin(['Crítica'])] 
all_mir7= all_mir6[['Service','inc_id']].groupby(['Service']).nunique()
#%%

Act_Data = [
    ['hello', 'world'],
    ['lukas', 'lukas'],
]
