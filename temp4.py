# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:43:05 2024

@author: aitor
"""

import pandas as pd
datos=pd.read_csv('ATP.csv')
df= pd.DataFrame(datos)
df.reset_index().to_csv('DatosExportadosATP.csv',header=True,index=False)
datos.set_index("Location", inplace=True)
df= datos.loc['Milan']
df.reset_index().to_csv('MilanSeleccATP.csv',header=True,index=False)
df2= datos.loc[datos['Series'].str.endswith("Slam")]
df2.reset_index().to_csv('GSSeleccATP.csv',header=True,index=False)
