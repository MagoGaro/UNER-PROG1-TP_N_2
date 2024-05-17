#Enunciado

#Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

#Solucion

def saludo(nombre):
    print(f"¡Hola {nombre}!")


#ejecucion
nombre = input("Ingrese su nombre: ")
saludo(nombre)