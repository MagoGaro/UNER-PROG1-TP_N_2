#Enunciado
"""
Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos 
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un 
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el 
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla 
el grupo que le corresponde

"""

#Solucion

def asignar_grupo(n, g):
    n = n[0].upper()
    
    if g.lower() == "m" and n < "M":
        grupo = "A"
    elif g.lower() == "h" and n > "N":
        grupo = "A"
    else:
        grupo = "B"

    print("Tu grupo es:", grupo)


#Ejecucion
nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu genero (H/M): ")


asignar_grupo(nombre,genero)


