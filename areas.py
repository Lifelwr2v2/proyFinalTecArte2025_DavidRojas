import math

def area(figura, m1, m2):
    if figura == 'c':
        return math.pi * (m1 ** 2)
    elif figura == 't':
        return (m1 * m2) / 2
    elif figura == 'r':
        return m1 * m2
    else:
        return 0
