import os
espera = []
sillon = []
silla = []

while True: 
    os.system('cls')
    print("1. Ingresar Cliente")
    print("2. Despertar al Barbero")
    print("3. Revisar Estado del Barbero")
    print("4. SALIR")

    opcion = int(input())

    if opcion == 1:
        ordenado()
    elif opcion == 2:
        corte()
    elif opcion == 3:
        estado()
        esperaa()
    elif opcion == 4:

        break
    else:
        print(" ")
        input("\nPresione tecla e Intentelo nuevament \n")


def ordenado():
    print(" \n Registra el listado de tus clientes \n ")
    x = input()

    if len(silla) == 0:
        silla.append(x)
    elif len(sillon) == 3:
        espera.append(x)
    elif len(sillon) < 3:
        sillon.append(x)

    print(" \n El Cliente ha sido registrado \n")
    input()

def corte():
    if len(silla) == 1:
        a = silla.pop()
        print("\n El barbero ha terminado con un cliente \n ")
        input()

        if len(sillon) > 0:
            y = sillon.pop(0)
            silla.append(y)
            print("\nEl babero esta atendiendo \n ")
            input()

        if len(espera) > 0:
            w = espera.pop(0)
            print("\n EL barbero atendio a \n")
            sillon.append(w)
        input()
    else:
        print("  \n Hora de una siesta... \n")
        input()
        
def estado():
    if len(silla) == 1:
        x = str(len(silla))
        print(" \nEl Barbero esta atendiendo\n ")
        input()
    elif len(silla) == 0:
        print(" \nEl Barbero esta durmiendo \n")
        input()
    elif len(silla) > 1:
        error23()

def clientess():
    a = len(silla)
    b = len(sillon)
    a = str(a)
    b = str(b)


    print(" \n Hay " + a + " esperando su turno")
    input()

