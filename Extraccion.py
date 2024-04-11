import pandas as pd

print('Aplicacion de estraccion de datos')
df = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx')
#print(df.info())
print(df.head())

#Filtro por objeto
filtro1 = df[df['NOMBRE_VENDEDOR'] == 'LETICIA RAMIREZ HERNANDEZ']
print(filtro1)
filtro1.to_csv('Entregable1.csv')

#Filtro por filas,
filtro2 = df.loc[2:8, : ]
print (filtro2)
filtro2.to_csv('Entregable2.csv')

#Filtro iloc
filtro3 = df.iloc[2:8, :]
print(filtro3)
filtro3.to_csv('Entregable3.csv')



df1 = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx', index_col=1)
#Filtro por fecha
filtro4=df1.loc[["2022-11-22","'2022-12-23"], ["SUBTOTAL_PARTIDA"]]
filtro4.to_csv('Entregable4.csv')

#Filtro primeros 5
filtro5=df.head(8)
filtro5.to_csv('Entregable5.csv')

#Filtro mayores a 77000
filtro6=df[df["SUBTOTAL_PARTIDA"] > 77000]
filtro6.to_csv('Entregable6.csv')

#Filtro precio y fecha
filtro7=df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
filtro7.to_csv('Entregable7.csv')

#Filtro precio y fecha 2
filtro8=df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
filtro8.to_csv('Entregable8.csv')

#Filtro not
filtro9=df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
filtro9.to_csv('Entregable9.csv')

