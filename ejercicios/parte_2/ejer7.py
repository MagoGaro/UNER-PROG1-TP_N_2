#Enunciado
"""
Que imprima todos los números entre el 100 y el 199.

"""

#Solucion

def impri_num():

    for i in range(100, 200):
        if i == 199: 
            print(f"{i}")
        else:
            print(f"{i}", end=" - ")


#ejecucion
impri_num()