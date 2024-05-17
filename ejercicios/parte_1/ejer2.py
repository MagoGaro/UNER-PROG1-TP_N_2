#Enunciado
"""
Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el
resultado.
"""

#Solucion

def ingreso_datos(frase1, frase2):
    num1 = input(f"{frase1} ")
    num2 = input(f"{frase2} ")
    return num1 , num2

def potencia(n1,n2):
    print(f"EL numero {n1} elevado a la potencia {n2} es: {n1**n2}")

def comprobacion_int():
    f1 = "Ingrese un numero entero positivo:"
    f2 = "Ingrese potencia:"
    while True:
        n1 , n2 = ingreso_datos(f1,f2)
        if (not (n1.isalpha()) and not (n2.isalpha())) and (n1.isdigit() and n2.isdigit()):
            return int(n1), int(n2)
        else:
            print("Solo se aceptan números enteros positivos")

#ejecucion

if __name__ == "__main__":
    potencia(*comprobacion_int())