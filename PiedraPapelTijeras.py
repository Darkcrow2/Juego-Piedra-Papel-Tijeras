import random

puntosUsuario = 0
puntosComputadora = 0

while True:
    opciones = ["piedra", "papel", "tijeras"]
    opcionesUsuario = input("Elige entre piedra, papel, tijeras o salir: ")
    opcionesComputadora = random.choice(opciones)

    if opcionesUsuario == "salir":
        print("JUEGO FINALIZADO")
        break;
    elif opcionesUsuario == "piedra":
        if opcionesComputadora == "piedra":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif opcionesComputadora == "papel":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif opcionesComputadora == "tijeras":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1
    elif opcionesUsuario == "papel":
        if opcionesComputadora == "papel":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif opcionesComputadora == "tijeras":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif opcionesComputadora == "piedra":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1
    elif opcionesUsuario == "tijeras":
        if opcionesComputadora == "tijeras":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nJuego empatado\n")
        elif opcionesComputadora == "piedra":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nComputadora gana\n")
            puntosComputadora = puntosComputadora + 1
        elif opcionesComputadora == "papel":
            print("Elegiste: ", opcionesUsuario, "\nLa computadora eligio: ", opcionesComputadora, "\nUsuario gana\n")
            puntosUsuario = puntosUsuario + 1

    if(puntosUsuario == 5):
        print("GANASTE EL DUELO CONTRA LA COMPUTADORA\n")
        break;
    elif(puntosComputadora == 5):
        print("PERDISTE EL DUELO CONTRA LA COMPUTADORA\n")
        break;
    else:
        print("El puntaje es", "\nUSUARIO: ", puntosUsuario, "\nCOMPUTADORA: ", puntosComputadora, "\n")


