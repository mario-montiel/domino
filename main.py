from domino.juego import Juego
import random
juego = Juego()
indice = 1
jugador = []
fichas = []
total_fichas = []
error = print("---- !! NO SE ENCONTRÓ NINGUNA BASE DE DATOS !! ----")
# HAGO LA CONEXIÓN A LA BASE DE DATOS
try:
    from database.db import Conexion
    db = Conexion()
    # OBTENER MULA
    juego.mula = db.obtener_mula()
    # OBTENGO DE LA CONSULTA TODAS LAS FICHAS Y LA GUARDO EN EL ARREGLO FICHAS DE FORMA ALEATORIA
    fichas = random.sample(db.database(1), k=28)
    #OBTENERMOS OTRA VEZ LAS FICHAS
    total_fichas = random.sample(db.database(1), k=28)
except:
    error
    
# REPARTIMOS LAS FICHAS A CADA JUGADOR
while indice != 5:
    nombre_jugadores = input("INGRESE EL NOMBRE DEL JUGADOR " + str(indice) + "\n")
    jugador.append(nombre_jugadores)
    # PASO LAS FICHAS ALEATORIAS OBTENIDAS DE LA BD A LA CLASE JUEGO
    juego.fichas = set(fichas)
    juego.repartir_fichas(indice, total_fichas)
    indice += 1

print("JUGADORES: " + str(jugador))

try:
    from database.db import Conexion
    db = Conexion()
    # MANDO EL NOMBRE DE LOS JUGADORES A LA CLASE DE LA BASE DE DATOS
    db.ingresar_jugadores(jugador)
    # OBTENGO DE LA CONSULTA TODAS LAS FICHAS Y LA GUARDO EN EL ARREGLO FICHAS DE FORMA ALEATORIA
    db.asignar_fichas_db(2, juego.fichas_jugador1, juego.fichas_jugador2, 
                             juego.fichas_jugador3, juego.fichas_jugador4, fichas)
    
    # ads
    # db.poner_ficha(3, juego.fichas_jugador1, juego.fichas_jugador2, 
    #                          juego.fichas_jugador3, juego.fichas_jugador4)
except:
    error
    
while juego.iniciar_mula != 1:
        turno = juego.poner_mula(total_fichas)
        
if turno == 5:
    turno = 1

print("EMPEZARÁ CON EL TURNO DEL JUGADOR " + str(turno))

# EMPEZAMOS A JUGAR UNA VEZ REPARTIDAS LAS FICHAS A CADA JUGADOR
while juego.victoria != 6:
    
    print("JUGADOR 1: " + str(juego.fichas_jugador1))
    print("JUGADOR 2: " + str(juego.fichas_jugador2))
    print("JUGADOR 3: " + str(juego.fichas_jugador3))
    print("JUGADOR 4: " + str(juego.fichas_jugador4))
    
    poner_ficha = int(input("Seleccione la ficha que desea poner.... JUGADOR " + str(turno) + "\n"))
    if turno == 1:
         # ENVIAMOS LA POSICIÓN QUE DESEAMOS ELIMINAR Y EL JUGADOR
        juego.poner_ficha(juego.fichas_jugador1[poner_ficha], turno)
    elif turno == 2:
        juego.poner_ficha(juego.fichas_jugador2[poner_ficha], turno)
    elif turno == 3:
        juego.poner_ficha(juego.fichas_jugador3[poner_ficha], turno)
    elif turno == 4:
        juego.poner_ficha(juego.fichas_jugador4[poner_ficha], turno)
        
    juego.victoria()
    turno += 1
    if turno == 5:
        turno = 1