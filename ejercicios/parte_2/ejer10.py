#Enunciado
"""
Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todos los números impares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último,su factorial.

"""

#Solucion

def comprobacion_int():
    while True:
        n1 = input("Ingrese un numero entero positivo: ")
        if not n1.isalpha() and n1.isdigit():
            return int(n1)
        else:
            print("Solo se aceptan números enteros positivos")

def imprimir_n(n):
    for i in range(1,(n+1),2):
        if i == (n) or i == (n-1):
            print(i)
        else:
            print(i, end=", ")

def imprimi_n_atras(n):
    for i in range((n),-1,-1):
        if i == 0:
            print(i)
        else:
            print(i, end=", ")

def es_primo(num, n=2):
    if n >= num:
        print("El número ingresado es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("El número ingresado no es primo")
        return False

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def compilar_n():
    num = comprobacion_int()
    imprimir_n(num)
    imprimi_n_atras(num)
    es_primo(num)
    print(f"El Factorial es: {factorial(num)}")


#ejecucion
compilar_n()