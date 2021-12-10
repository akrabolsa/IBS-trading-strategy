 # -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:56:48 2021

@author: Usuario
"""

#%%We get data

import yfinance as yf
from datetime import date,timedelta
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

def_figsize = (10, 5)

dias_atras=20*365
stock="^GDAXI"

data_yahoo = yf.download(stock, start=date.today()-timedelta(days=dias_atras), end=date.today(), group_by="ticker")
#Seleccionamos de la descarga lo que queremos y lo ordenamos igual que los datos que tenemos
del dias_atras

data=data_yahoo.iloc[:,0:4]

del data_yahoo
data=data.fillna(method='ffill')
data=data.dropna()

#Calculate IBS indicator:

data['IBS']=(data.Close-data.Low)/(data.High-data.Low)

#CAlculate returns

data['ret']=np.log(data.Close) - np.log(data.Close.shift(1))

#Calculate  Signal
data['Signal']=0

data.Signal=np.where(data.IBS.shift(1)<0.25,1,0)

data.Signal=np.where(data.IBS.shift(1)>0.75,-1,data.Signal)

#WE calculate strategy's return

data['IBS_ret']=data.ret*data.Signal


data['Index']=(1+data.ret).cumprod()
data['Strategy']=(1+data.IBS_ret).cumprod()


data['Index'].plot(label="Index")
data['Strategy'].plot(label="Strategy")
plt.gcf().autofmt_xdate()
plt.legend(loc='best')
plt.show()
