from random import *
class Juego:
    fichas_jugador1 = []
    fichas_jugador2 = []
    fichas_jugador3 = []
    fichas_jugador4 = []
    fichas = set(["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete",
                  "yyuno", "yydos", "yytres", "yycuatro", "yycinco", "yyseis", "yysiete",
                  "xxuno", "xxdos", "xxtres", "xxcuatro", "xxcinco", "xxseis", "xxsiete", 
                  "ppuno", "ppdos", "pptres", "ppcuatro", "ppcinco", "ppseis", "ppsiete"])
    def jugadores(self, nombre_jugador):
        jugador = []
        jugador.append(nombre_jugador)
        return jugador
    
    def repartir_fichas(self, jugador):
        
        
        indice = 1
        while indice != 8:
            # SE ELIMINAN LAS FICHAS
            ficha_eliminada = self.fichas.pop()
            print(self.fichas)
            print(ficha_eliminada)
            
            # SE REPARTEN LAS FICHAS DEPENDIENDO EL NÚMERO DEL JUGADOR
            if jugador == 1:
                self.fichas_jugador1.append(ficha_eliminada)
            elif jugador == 2:
                self.fichas_jugador2.append(ficha_eliminada)
            elif jugador == 3:
                self.fichas_jugador3.append(ficha_eliminada)
            elif jugador == 4:
                self.fichas_jugador4.append(ficha_eliminada)
            indice += 1
        obtener_fichas_jugador=[]
        print("FICHAS DEL JUGADOR 1: " + str(self.fichas_jugador1))
        print("FICHAS DEL JUGADOR 2: " + str(self.fichas_jugador2))
        print("FICHAS DEL JUGADOR 3: " + str(self.fichas_jugador3))
        print("FICHAS DEL JUGADOR 4: " + str(self.fichas_jugador4))
        
        