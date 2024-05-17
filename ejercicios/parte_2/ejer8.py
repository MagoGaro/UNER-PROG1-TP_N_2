#Enunciado
"""
 Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""

#Solucion

def validar_edad(x):

    if x > 17:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")

    
#ejecucion
edad = input("Ingrese su edad: ")

validar_edad(int(edad))