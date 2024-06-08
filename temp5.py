# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:11:26 2024

@author: aitor
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.head)
datos.set_index("Location",inplace=True)
print(datos.loc[datos['Court']=='Outdoor',['Surface']])
print(datos.loc[datos['Court']=='Outdoor',['Surface','Winner']])
print("*******************MÁS DE UNA CONDICIÓN********************")
print(datos.loc[datos['Series'].str.endswith("Slam")&(datos['Surface']=='Clay')&(datos['Winner']=='Federer R.')&(datos['Round']=='The Final')])
