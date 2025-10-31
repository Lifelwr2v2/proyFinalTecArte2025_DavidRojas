import pandas as pd

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	print(f"Fila {index}: Figura = {row['Figura']}, Medida 1 = {row['Medida1']}, Medida 2 = {row['Medida2']}")



