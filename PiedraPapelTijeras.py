import random

class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.puntosUsuario = 0
        self.puntosComputadora = 0

        print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERAS\n") #Bienvenida del juego

    def jugar(self):

        while True:
            opciones = ["piedra", "papel", "tijeras", "salir"]
            opcionesUsuario = input(f"Elige entre {opciones[0]}, {opciones[1]}, {opciones[2]} y {opciones[3]}: ")
            opcionesComputadora = random.choice(opciones)

            if (opcionesUsuario.lower() == opciones[3].lower()):
                print("\nJUEGO FINALIZADO")
                print(f"EL PUNTAJE ES \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")
                break;
            elif (opcionesUsuario.lower() == opciones[0].lower()):
                if (opcionesComputadora.lower() == opciones[0].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                elif (opcionesComputadora.lower() == opciones[1].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                    self.puntosComputadora = self.puntosComputadora + 1
                elif(opcionesComputadora.lower() == opciones[2].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                    self.puntosUsuario = self.puntosUsuario + 1
            elif (opcionesUsuario.lower() == opciones[1].lower()):
                if (opcionesComputadora.lower() == opciones[1].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                elif (opcionesComputadora.lower() == opciones[2].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                    self.puntosComputadora = self.puntosComputadora + 1
                elif (opcionesComputadora.lower() == opciones[0].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                    self.puntosUsuario = self.puntosUsuario + 1
            elif (opcionesUsuario.lower() == opciones[2].lower()):
                if (opcionesComputadora.lower() == opciones[2].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                elif (opcionesComputadora.lower() == opciones[0].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                    self.puntosComputadora = self.puntosComputadora + 1
                elif (opcionesComputadora.lower() == opciones[1].lower()):
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                    self.puntosUsuario = self.puntosUsuario + 1

            if(self.puntosUsuario == 5):
                print("GANASTE LA BATALLA CONTRA LA COMPUTADORA\n")
                break;
            elif(self.puntosComputadora == 5):
                print("PERDISTE LA BATALLA CONTRA LA COMPUTADORA\n")
                break;
            else:
                print(f"EL PUNTAJE ES \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")

JuegoPiedraPapelTijeras().jugar()