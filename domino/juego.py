from random import *
import pygame
from pygame.locals import *
class Juego:
    fichas_jugador1 = []
    fichas_jugador2 = []
    fichas_jugador3 = []
    fichas_jugador4 = []
    ultima_ficha_puesta = []
    # puntuacion_j_1 = 0
    # puntuacion_j_2 = 0
    # puntuacion_j_3 = 0
    # puntuacion_j_4 = 0
    victoria = 1
    fichas = []
    mula = []
    iniciar_mula = 0
    turno = 0
    
    def jugadores(self, nombre_jugador):
        jugador = []
        jugador.append(nombre_jugador)
        return jugador
    
    def repartir_fichas(self, jugador, fichas):
        # SE REPARTEN LAS FICHAS DEPENDIENDO EL NÚMERO DEL JUGADOR
        for i in fichas:
            if jugador == 1 and i[4] == 1:
                self.fichas_jugador1.append(i)
            elif jugador == 2 and i[4] == 2:
                self.fichas_jugador2.append(i)
            elif jugador == 3 and i[4] == 3:
                self.fichas_jugador3.append(i)
            elif jugador == 4 and i[4] == 4:
                self.fichas_jugador4.append(i)
            
        # print("FICHAS DEL JUGADOR 1: " + str(self.fichas_jugador1))
        # print("FICHAS DEL JUGADOR 2: " + str(self.fichas_jugador2))
        # print("FICHAS DEL JUGADOR 3: " + str(self.fichas_jugador3))
        # print("FICHAS DEL JUGADOR 4: " + str(self.fichas_jugador4))
        
    def poner_mula(self, fichas):
        
        for i in self.fichas_jugador1:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador1.remove(i)
                self.ultima_ficha_puesta = i
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return i[4]
            
        for i in self.fichas_jugador2:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador2.remove(i)
                self.ultima_ficha_puesta = i
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return i[4]
            
        for i in self.fichas_jugador3:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador3.remove(i)
                self.ultima_ficha_puesta = i
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return i[4]
            
        for i in self.fichas_jugador4:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador4.remove(i)
                self.ultima_ficha_puesta = i
                print("\nÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return i[4]
        
    def poner_ficha(self, click, jugador):
        # COMPARO FICHA Y LA ELIMINO A LA VERGA!!!
        if click[2] == self.ultima_ficha_puesta[2] or click[3] == self.ultima_ficha_puesta[3] or click[2] == self.ultima_ficha_puesta[3] or click[3] == self.ultima_ficha_puesta[2]:
            self.ultima_ficha_puesta = click
            print("FICHA CORRECTA")
            print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
            if jugador == 1:
                self.fichas_jugador1.remove(click)
            elif jugador == 2:
                self.fichas_jugador2.remove(click)
            elif jugador == 3:
                self.fichas_jugador3.remove(click)
            elif jugador == 4:
                self.fichas_jugador4.remove(click)
        else:
            print("FICHA INCORRECTA")
            print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
            
        
        
    def victoria(self):
        if len(self.fichas_jugador1) <= 0:
            print("GANÓ JUGADOR 1")
            self.victoria = 6
        elif len(self.fichas_jugador2) <= 0:
            print("GANÓ JUGADOR 2")
            self.victoria = 6
        elif len(self.fichas_jugador3) <= 0:
            print("GANÓ JUGADOR 3")
            self.victoria = 6
        elif len(self.fichas_jugador4) <= 0:
            print("GANÓ JUGADOR 4")
            self.victoria = 6
            
    # def puntuacion(self):
    #     if 