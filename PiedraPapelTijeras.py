import random

class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.puntosUsuario = 0
        self.puntosComputadora = 0
        self.ganador = False
        self.opciones = ["PIEDRA", "PAPEL", "TIJERAS", "SALIR"]

    def jugar(self):

        print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERAS\n")

        while True:
            
            opcionesUsuario = input(f"Elige entre {self.opciones[0]}, {self.opciones[1]}, {self.opciones[2]} y {self.opciones[3]}: ").upper()
            opcionesComputadora = self.opciones[random.randint(0, 2)]

            if (opcionesUsuario == self.opciones[3]):
                print("\nJUEGO FINALIZADO")
                print(f"EL PUNTAJE ES: \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")
                break;
            elif (opcionesUsuario == self.opciones[0]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1

                self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
                if(self.ganador):
                    break

            elif (opcionesUsuario == self.opciones[1]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1

                self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
                if(self.ganador):
                    break

            elif (opcionesUsuario == self.opciones[2]):
                match opcionesComputadora.lower():
                    case "piedra":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora gana\n")
                        self.puntosComputadora = self.puntosComputadora + 1
                    case "papel":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario gana\n")
                        self.puntosUsuario = self.puntosUsuario + 1
                    case "tijeras":
                        print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego empatado\n")

                self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
                if(self.ganador):
                    break

            else:
                print("Por favor, seleccione una opcion valida\n")

    def puntaje(self, puntosUsuario, puntosComputadora):
        if(puntosUsuario == 5):
            print("GANASTE LA BATALLA CONTRA LA COMPUTADORA\n")
            return True
        elif(puntosComputadora == 5):
            print("PERDISTE LA BATALLA CONTRA LA COMPUTADORA\n")
            return True
        else:
            print(f"EL PUNTAJE ES: \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")
            return False

JuegoPiedraPapelTijeras().jugar()