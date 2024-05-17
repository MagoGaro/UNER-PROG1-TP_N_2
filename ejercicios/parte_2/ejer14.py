#Enunciado
"""
Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son 
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos 
ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 
no es bisiesto

"""

#Solucion
def es_biciesto(a):
 
    if a % 4 != 0:
        return False


    if a % 100 == 0 and a % 400 != 0:
        return False


    return True


def main():

    a = int(input("Ingrese un año: "))

 
    if es_biciesto(a):
        print(f"{a} es año biciesto.")
    else:
        print(f"el {a} no es año biciesto.")


#Ejecucion
main()