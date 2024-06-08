# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:54:49 2024

@author: aitor
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.info())
print(datos.head())
print(datos.iloc[0:20])
print(datos.iloc[[0,3,3,6,24],])
#Columnas
print(datos.iloc[:,0:2])
print(datos.iloc[[0,3,6,24],[0,5,6]])
print(datos.iloc[0:5,0:5])
