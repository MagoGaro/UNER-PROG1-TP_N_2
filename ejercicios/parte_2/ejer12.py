#Enunciado
"""
Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro 
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día 
ingresado no es ninguno de esos, imprimir otro mensaje

"""

#Solucion

dias_semana = ("lunes","martes","miercoles","miércoles","jueves","viernes","sabado","sábado","domingo")

def comprobar_dia():
    dia = input("Ingrese un día de la semana: ").lower()
    if dia in dias_semana:
        return dia


def enviar_msg():
    while True:
        x = comprobar_dia()
        if x == dias_semana[0]:
            print("Uff.. Lunes otra vez")
            break
        elif x == dias_semana[5]:
            print("Vamo lo pibe que es Viernes !!")
            break
        elif x == dias_semana[6] or  x == dias_semana[7] or x == dias_semana[8]:
            print("Que bueno que es fin de semana")
            break
        elif x == None:
            print("Ese día no existe.")
        else:
            print(f"hoy es {x} ya falta menos para el viernes")
            break

#Ejecucion
enviar_msg()