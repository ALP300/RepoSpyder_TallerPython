# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:14:47 2024

@author: aitor
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.head())
datos.set_index("Location", inplace=True)
print("Milan")
print(datos.loc['Milan'])
print("Atlanta y Superficie")
print(datos.loc['Atlanta','Surface'])
print("Selección amplia")
print(datos.loc[['Atlanta','Milan'],
['Series','Court','Loser']])
print("Selección con rango")
print(datos.loc[['Atlanta','Milan'],'Series':'Round'])
print("Selección solamente de Slam")
print(datos.loc[datos['Series'].str.endswith("Slam")])
