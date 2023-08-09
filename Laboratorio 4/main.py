import pandas as pd
import matplotlib.pyplot as plt



#Creando el dataframe usando los datos del archivo
df=pd.read_csv(r'C:\Users\ricardo.quiros\Documents\Clases progra\Python\UCR\Python_2\Python-2\Laboratorio 4\ventas.csv')

#Agregando la nueva columna calculada
df['Ganacia']=df['Ventas']-df['Gastos']

#Extrayendo los datos de las columnas en forma de lista para poder utilizarlo en matplot
"""
for mes in df['Mes'].values.tolist():
    size=len(mes)
    mes_corto=mes[:size-3]
"""

ejeX= df['Mes'].values.tolist()
linea_1=df['Gastos'].values.tolist()
linea_2=df['Ventas'].values.tolist()


fig,ax=plt.subplots()
ax.plot(ejeX,linea_1, label='Gastos')
ax.plot(ejeX,linea_2, label='Ventas')
ax.legend(loc='upper right')
plt.title('Evolucion mensual de Ventas y Gastos')
plt.xlabel('Mes')
plt.ylabel('Ventas vs Gastos')


#plt.plot(ejeX,linea_1)
plt.show()
#print(data)
