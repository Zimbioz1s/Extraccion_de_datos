
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('datos_facturacion.xlsx')

print(df.head())

filtro1 = df [ (df['CVE_CLPV']>= 1000) & (df['CVE_CLPV']<=2000)]
filtro1.to_csv('practica_facturacion.csv')

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
filtro2

filtro3=df[df["FECHA_ENT"] == '2022-28-2']
filtro3

filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
filtro4

filtro5 = df.iloc[ : , [0, 6, 7,9]]  
filtro5

filtro6 = df.iloc[7001:7099, :  ] 
filtro6

df1= pd.read_excel('datos_facturacion.xlsx', index_col=3)
df1.head()

filtro7=df1.loc[[1.0,2.0], ["FECHAELAB"]]
filtro7

filtro1.to_csv("practica_facturacion_1.csv")
filtro1.to_csv("practica_facturacion_2.csv")
filtro1.to_csv("practica_facturacion_3.csv")
filtro1.to_csv("practica_facturacion_4.csv")
filtro1.to_csv("practica_facturacion_5.csv")
filtro1.to_csv("practica_facturacion_6.csv")
filtro1.to_csv("practica_facturacion_7.csv")