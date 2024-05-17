#Enunciado
"""
Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se 
encuentran en dicha frase.

"""

#Solucion

def contar_vocales(frase):
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    print(f"Su frase tiene: {sum([1 for letra in frase if letra in vocales])} vocales")

#Ejecución
frase = input("Ingrese una frase: ")
contar_vocales(frase)

