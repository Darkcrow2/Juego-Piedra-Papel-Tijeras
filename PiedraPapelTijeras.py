import random

class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.puntosUsuario = 0
        self.puntosComputadora = 0

        print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERAS\n") #Bienvenida del juego

    def jugar(self):

        while True:
            opciones = ["piedra", "papel", "tijeras"]
            opcionSalir = "salir"
            opcionesUsuario = input(f"Elige entre {opciones[0].upper()}, {opciones[1].upper()}, {opciones[2].upper()} y {opcionSalir.upper()}: ").upper()
            opcionesComputadora = random.choice(opciones).upper()

            if (opcionesUsuario.lower() == opcionSalir):
                print("\nJUEGO FINALIZADO")
                print(f"EL PUNTAJE ES: \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")
                break;
            elif (opcionesUsuario.lower() == opciones[0]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1
            elif (opcionesUsuario.lower() == opciones[1]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1
            elif (opcionesUsuario.lower() == opciones[2]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")

            if(self.puntosUsuario == 5):
                print("GANASTE LA BATALLA CONTRA LA COMPUTADORA\n")
                break;
            elif(self.puntosComputadora == 5):
                print("PERDISTE LA BATALLA CONTRA LA COMPUTADORA\n")
                break;
            else:
                print(f"EL PUNTAJE ES: \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")

JuegoPiedraPapelTijeras().jugar()