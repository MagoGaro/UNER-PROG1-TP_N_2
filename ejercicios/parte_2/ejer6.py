#Enunciado
"""
Que pida al usuario una palabra y la muestre por pantalla 10 veces.

"""

#Solucion

def repetirPalabra():
    palabra = ""
    control = True
    while control:
        palabra = input("Ingrese una plabra: ")

        if palabra == '':
            print("Debe ingresar una palabra.")
        else:
            control = False
    
    print(f"{(palabra+" ")*10}")

    
#ejecucion

repetirPalabra()
