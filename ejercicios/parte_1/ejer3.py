#Enunciado
"""
Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%
"""

#Solucion
from ejer2 import ingreso_datos

def comprobacion_dec():
    f1 = "Ingrese monto de la factura sin IVA:"
    f2 = "Ingrese porcentaje del IVA:"
    while True:
        n1 , n2 = ingreso_datos(f1,f2)
        if not (n1.isalpha()) and not (n2.isalpha()):
            if n2 != "":
                return float(n1) , float(n2)
            else:
                return float(n1) , 21
        else:
            print("Solo se aceptan números positivos")
        
def calcularFac(cant,iva):
    print(cant,iva)
    iva = (iva / 100) +1
    total = cant * iva
    print(f"El total de la factura con IVA es: {total}")


#ejecucion

if __name__ == "__main__":
    calcularFac(*comprobacion_dec())
