from domino.juego import Juego
juego = Juego()
indice = 1
jugador = []
fichas = []
# HAGO LA CONEXIÓN A LA BASE DE DATOS
try:
    from database.db import Conexion
    db = Conexion()
    # OBTENGO DE LA CONSULTA TODAS LAS FICHAS Y LA GUARDO EN EL ARREGLO FICHAS DE FORMA ALEATORIA
    fichas = set(db.database(1))
except:
    print("---- !! NO SE ENCONTRÓ NINGUNA BASE DE DATOS !! ----")
    
# REPARTIMOS LAS FICHAS A CADA JUGADOR
while indice != 5:
    nombre_jugadores = input("INGRESE EL NOMBRE DEL JUGADOR " + str(indice) + "\n")
    jugador.append(juego.jugadores(nombre_jugadores))
    # PASO LAS FICHAS ALEATORIAS OBTENIDAS DE LA BD A LA CLASE JUEGO
    juego.fichas = fichas
    juego.repartir_fichas(indice)
    indice += 1

indice = 1
print("JUGADORES: " + str(jugador))

# EMPEZAMOS A JUGAR UNA VEZ REPARTIDAS LAS FICHAS A CADA JUGADOR
while juego.victoria != 6:
    print("JUGADOR 1: " + str(juego.fichas_jugador1))
    print("JUGADOR 2: " + str(juego.fichas_jugador2))
    print("JUGADOR 3: " + str(juego.fichas_jugador3))
    print("JUGADOR 4: " + str(juego.fichas_jugador4))
    poner_ficha = int(input("Seleccione la ficha que desea poner"))
    if indice == 1:
        # ENVIAMOS LA POSICIÓN QUE DESEAMOS ELIMINAR Y EL JUGADOR
        juego.poner_ficha(juego.fichas_jugador1[poner_ficha], indice)
    elif indice == 2:
        juego.poner_ficha(juego.fichas_jugador2[poner_ficha], indice)
    elif indice == 3:
        juego.poner_ficha(juego.fichas_jugador3[poner_ficha], indice)
    elif indice == 4:
        juego.poner_ficha(juego.fichas_jugador4[poner_ficha], indice)
    juego.victoria()
    indice += 1
    if indice == 5:
        indice = 1

    