from domino.juego import Juego
juego = Juego()
indice = 1
jugador = []
while indice != 5:
    nombre_jugadores = input("INGRESE EL NOMBRE DEL JUGADOR " + str(indice) + "\n")
    jugador.append(juego.jugadores(nombre_jugadores))
    juego.repartir_fichas(indice)
    indice += 1
print(jugador)
    