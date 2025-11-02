import math #Se importa la libreria math para poder ocupar a 'pi'

def area(figura, m1, m2): #Se define la función 'area' la cual se importa en figurasPrincipal.py para calcular las areas
    #Se le pasa como argumentos, la letra correspondiente a la figura, la medida 1 y la medida 2
    if figura == 'c': 
        return math.pi * (m1 ** 2) #Si la figura es un circulo 'c', se calcula con la fórmula de área del circulo, retorna el resultado
    elif figura == 't': 
        return (m1 * m2) / 2 # Si es un triángulo se calcula con la fórmula de área del triangulo, retorna el resultado
    elif figura == 'r':
        return m1 * m2 # Si es un rectángulo se calcula con la fórmula de área del rectángulo, retorna el resultado
    else:
        return 0 #Caso de que no sea ninguna de las 3 retorna 0
