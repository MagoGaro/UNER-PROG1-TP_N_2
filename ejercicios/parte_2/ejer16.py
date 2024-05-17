#Enunciado
"""
 Que imprima el siguiente patrón: 

        54321
        4321
        321
        21
        1
  

"""

#Solucion
def imprimir_patron(n):
    n1 = n
    n2 = n

    for i in range(n1):
        for j in range(n2, 0, -1):
            print(j, end="")
        print()
        n2 -= 1

#Ejecucion

imprimir_patron(int(input("Ingrese un numero: ")))