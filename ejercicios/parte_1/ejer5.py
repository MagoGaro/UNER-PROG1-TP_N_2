#Enunciado
"""
Que dado tres números ingresados por el usuario nos devuelva el promedio.

"""

#Solucion

def calcularPro():
    sum = 0
    for i in range(3):
        n = float(input(f"Ingrese el N° {i+1}: "))
        sum += n
    return sum / 3

#ejecucion

print(f"El promedio es: {calcularPro()}")