import random

puntosUsuario = 0
puntosComputadora = 0

print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERAS\n") #Bienvenida del juego

while True:
    opciones = ["piedra", "papel", "tijeras"]
    opcionesUsuario = input("Elige entre piedra, papel, tijeras o salir: ")
    opcionesComputadora = random.choice(opciones)

    if (opcionesUsuario.lower() == "salir".lower()):
        print("JUEGO FINALIZADO")
        break;
    elif (opcionesUsuario.lower() == "piedra".lower()):
        if (opcionesComputadora.lower() == "piedra".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif (opcionesComputadora.lower() == "papel".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif (opcionesComputadora.lower() == "tijeras".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1
    elif (opcionesUsuario.lower() == "papel".lower()):
        if (opcionesComputadora.lower() == "papel".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif (opcionesComputadora.lower() == "tijeras".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif (opcionesComputadora.lower() == "piedra".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1
    elif (opcionesUsuario.lower() == "tijeras".lower()):
        if (opcionesComputadora.lower() == "tijeras".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif (opcionesComputadora.lower() == "piedra".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif (opcionesComputadora.lower() == "papel".lower()):
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1

    if(puntosUsuario == 5):
        print("GANASTE LA BATALLA CONTRA LA COMPUTADORA\n")
        break;
    elif(puntosComputadora == 5):
        print("PERDISTE LA BATALLA CONTRA LA COMPUTADORA\n")
        break;
    else:
        print("El puntaje es", "\nUSUARIO: ", puntosUsuario, "\nCOMPUTADORA: ", puntosComputadora, "\n")


