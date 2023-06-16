import random

class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.puntosUsuario = 0
        self.puntosComputadora = 0
        self.ganador = False
        self.opciones = ["PIEDRA", "PAPEL", "TIJERAS", "SALIR"]
        print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERAS\n")

    def jugar(self):

        opcionesUsuario = input(f"Elige entre {self.opciones[0]}, {self.opciones[1]}, {self.opciones[2]} y {self.opciones[3]}: ").upper()
        opcionesComputadora = self.opciones[random.randint(0, 2)]

        if (opcionesUsuario == self.opciones[3]):
            print("\nJUEGO FINALIZADO")
            print(f"EL PUNTAJE ES: \nUsuario: {self.puntosUsuario} \nComputadora: {self.puntosComputadora} \n")
        elif (opcionesUsuario == self.opciones[0]):
            match opcionesComputadora.lower():
                case "piedra":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego EMPATADO\n")
                case "papel":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora GANA\n")
                    self.puntosComputadora = self.puntosComputadora + 1
                case "tijeras":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario GANA\n")
                    self.puntosUsuario = self.puntosUsuario + 1

            self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
            if(self.ganador != True):
                return self.jugar()

        elif (opcionesUsuario == self.opciones[1]):
            match opcionesComputadora.lower():
                case "piedra":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario GANA\n")
                    self.puntosUsuario = self.puntosUsuario + 1
                case "papel":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego EMPATADO\n")
                case "tijeras":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora GANA\n")
                    self.puntosComputadora = self.puntosComputadora + 1

            self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
            if(self.ganador != True):
                return self.jugar()

        elif (opcionesUsuario == self.opciones[2]):
            match opcionesComputadora.lower():
                case "piedra":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nComputadora GANA\n")
                    self.puntosComputadora = self.puntosComputadora + 1
                case "papel":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nUsuario GANA\n")
                    self.puntosUsuario = self.puntosUsuario + 1
                case "tijeras":
                    print(f"\nElegiste: {opcionesUsuario} \nLa computadora eligio: {opcionesComputadora} \nJuego EMPATADO\n")

            self.ganador = self.puntaje(self.puntosUsuario, self.puntosComputadora)
            if(self.ganador != True):
                return self.jugar()

        else:
            print("Por favor, seleccione una opcion valida\n")
            return self.jugar()

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