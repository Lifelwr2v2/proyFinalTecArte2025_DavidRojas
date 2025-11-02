import pandas as pd
from areas import area #Del archivo areas importamos la funcion area

dataFile = pd.read_csv('figuras.csv', sep = r'\s+') #Se modificó el codigo para que leeyera el datafile separado por espacios

print("Procesando figuras...\n") # Mensaje de encabezado para indicar lo que se está haciendo

areas = [] # Se inicializa una lista vacia de nombre 'areas'
perimetros = [] # Se inicializa una lista vacia de nombre 'perimetros'

for index, row in dataFile.iterrows(): # Se inicializa un ciclo for que itera sobre cada fila de cada índice del datafile
	figura = row['FIGURA'] # Se le asigna el valor que esté en la fila de Figura a 'figura'
	m1 = row['MEDIDA1'] # Se le asigna el valor que esté en la fila de MEDIDA1 a 'm1'
	m2 = row['MEDIDA2'] # Se le asigna el valor que esté en la fila de MEDIDA1 a 'm2'
	a = area(figura, m1, m2)
        # Lo que retorne la función 'area' al pasarle los parámetros figura, m1, m2 se guardará en la variable 'a'
	areas.append(a) # Se agrega el valor de 'a' a la lista 'areas'
	print(f"Fila {index}: Figura = {row['FIGURA']}, Medida1 = {row['MEDIDA1']}, Medida2 = {row['MEDIDA2']}, Area = {a}")
        # Se imprime como f-string la figura que es, sus medidas y su área
