#Enunciado
"""
Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
en que ambos números son iguales.
"""

#Solucion

def comprar_num(x1,x2):

    if x1 > x2:
        print(f"El menor es: {x2}")
    elif x1 == x2:
        print(f"Ambos numeros son iguales")
    else:
        print(f"El menor es: {x1}")

    
#ejecucion
n1 = input("Ingrese un numero: ")
n2 = input("Ingrese otro numero: ")

comprar_num(n1,n2)