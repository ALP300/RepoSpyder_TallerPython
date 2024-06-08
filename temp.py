# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
import numpy as np

datos={'Nombre':['Chalio','Juan','Leo','Carlo','Valentina'],
       'Calificaciones':['100','50','30','51','99'],
        'Deportes':['Fútbol','Básquet','Rugby','Balon mano','Voley'],
        'Materias':['Calculo','Metodos','Fisica','Quimica','Programacion']}


df= pd.DataFrame(datos)
print(df)
print('\n'*2)

datos2= {'Nombre':['Chalio','Juan','N/A','Carlo','Valentina'],
         'Calificaciones':['100','50','30','51',np.nan],
         'Deportes':['Fútbol','Básquet','N/A','Balon mano','Voley'],
         'Materias':['Calculo','Metodos','Fisica','N/A','Programacion']}

df2= pd.DataFrame(datos2)
print(df2)
print('\n'*2)

print(df2.info())
print('\n'*4)

print(df2.describe())
print('\n'*4)

nuevo= pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo)