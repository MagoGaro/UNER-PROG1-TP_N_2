#Enunciado
"""
Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay

"""

#Solucion

def buscador_n_primos():
    cont = 0
    for n in range(2, 101):
        es_primo = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break

        if es_primo:
            print(n, end=" ")
            cont += 1
            
    print(f"\nTotal de numeros primos encontrados en el rango 0 a 100: {cont}")



#Ejecucion
buscador_n_primos()