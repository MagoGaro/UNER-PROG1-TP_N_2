#Enunciado
"""
Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe 
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato

"""

#Solucion

def es_vocal():
    
    while True:
        c = input("Ingrese un caracter: ")
        if len(c) != 1:
            print("No se puede procesar el dato.")
        else:
            break

    if c.lower() in "aeiou":
        print(c, "es vocal.")
    else:
        print(c, "np es vocal.")


#Ejecucion

es_vocal()