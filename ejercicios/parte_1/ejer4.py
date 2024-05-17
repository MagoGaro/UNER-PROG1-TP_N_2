#Enunciado
"""
Que dada la base y altura de un triángulo nos calcule su área
"""

#Solucion

from ejer2 import ingreso_datos

def comprobacion_valor():
    f1 = "Ingrese la base de un triángulo:"
    f2 = "Ingrese la altura de un triángulo:"
    while True:
        n1 , n2 = ingreso_datos(f1,f2)
        if not (n1.isalpha()) and not (n2.isalpha()):
            return float(n1), float(n2)
        else:
            print("Solo se aceptan números positivos")

def calcularArea(base,alt):
    area = 0
    area = (base*alt)/2
    return area

#ejecucion

if __name__ == "__main__":
    print(f"El area del Triangulo es: {calcularArea(*comprobacion_valor())}")

