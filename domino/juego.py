from random import *
import pygame
from pygame.locals import *
class Juego:
    fichas_jugador1 = []
    fichas_jugador2 = []
    fichas_jugador3 = []
    fichas_jugador4 = []
    ultima_ficha_puesta = []
    izquierda = []
    derecha = []
    copiaclickiz = []
    copiaclickde = []
    fichamentira = [6,6]
    fichaseliminadas = []
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
        # print(fichas[0:7])
        iteracion = 1
        for i in fichas:
            if jugador == 1 and iteracion < 8:
                self.fichas_jugador1.append(i)
                print(self.fichas_jugador1)
            elif jugador == 2 and iteracion < 15 and iteracion > 7:
                self.fichas_jugador2.append(i)
                print(self.fichas_jugador2)
            elif jugador == 3 and iteracion < 22 and iteracion > 14:
                self.fichas_jugador3.append(i)
                print(self.fichas_jugador3)
            elif jugador == 4 and iteracion > 21:
                self.fichas_jugador4.append(i)
                print(self.fichas_jugador4)
            iteracion += 1
            
        print("FICHAS DEL JUGADOR 1: " + str(self.fichas_jugador1))
        print("FICHAS DEL JUGADOR 2: " + str(self.fichas_jugador2))
        print("FICHAS DEL JUGADOR 3: " + str(self.fichas_jugador3))
        print("FICHAS DEL JUGADOR 4: " + str(self.fichas_jugador4))
        
    def poner_mula(self, fichas):
        # print(fichas)
        for i in self.fichas_jugador1:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador1.remove(i)
                self.ultima_ficha_puesta = i
                self.fichaseliminadas.append(i)
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return 2
            
        for i in self.fichas_jugador2:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador2.remove(i)
                self.ultima_ficha_puesta = i
                self.fichaseliminadas.append(i)
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return 3
            
        for i in self.fichas_jugador3:
            if i[0] == 28:
                self.turno = i[4]
                self.fichas_jugador3.remove(i)
                self.ultima_ficha_puesta = i
                self.fichaseliminadas.append(i)
                print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return 4
            
        for i in self.fichas_jugador4:
            if i[0] == 28:
                self.turno = i[4]
                # print(i[])
                self.fichas_jugador4.remove(i)
                self.ultima_ficha_puesta = i
                self.fichaseliminadas.append(i)
                print("\nÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
                self.iniciar_mula = 1
                return 1
        
    def poner_ficha(self, click, jugador, klado):
        # COMPARO FICHA Y LA ELIMINO A LA VERGA!!!
        contador = 0
        if klado== "d":
            if click[2] == self.fichamentira[0]:
                objeto = []
                for x in click:
                    contador += 1
                    if contador < 5:
                        objeto.append(x)
                    else:
                        objeto.append("derecha")
                self.copiaclickde.append(objeto)
                # copiaclick[5] = "derecha"
                self.izquierda.append(click)
                self.fichamentira[0] = click[3]
                if jugador == 1:
                    self.fichas_jugador1.remove(click)
                elif jugador == 2:
                    self.fichas_jugador2.remove(click)
                elif jugador == 3:
                    self.fichas_jugador3.remove(click)
                elif jugador == 4:
                    self.fichas_jugador4.remove(click)
            elif click[3] == self.fichamentira[1]:
                objeto = []
                for x in click:
                    contador += 1
                    if contador < 5:
                        objeto.append(x)
                    else:
                        objeto.append("derecha")
                self.copiaclickde.append(objeto)
                # copiaclick[5] = "derecha"
                self.derecha.append(click)
                self.fichamentira[1] = click[2]
                if jugador == 1:
                    self.fichas_jugador1.remove(click)
                elif jugador == 2:
                    self.fichas_jugador2.remove(click)
                elif jugador == 3:
                    self.fichas_jugador3.remove(click)
                elif jugador == 4:
                    self.fichas_jugador4.remove(click)
        elif klado == "i":
            if click[2] == self.fichamentira[1]:
                objeto = []
                for x in click:
                    contador += 1
                    if contador < 5:
                        objeto.append(x)
                    else:
                        objeto.append("izquierda")
                self.copiaclickiz.append(objeto)
                # copiaclick[5] = "izquierda"
                self.derecha.append(click)
                self.fichamentira[1] = click[3]
                if jugador == 1:
                    self.fichas_jugador1.remove(click)
                elif jugador == 2:
                    self.fichas_jugador2.remove(click)
                elif jugador == 3:
                    self.fichas_jugador3.remove(click)
                elif jugador == 4:
                    self.fichas_jugador4.remove(click)
            elif click[3] == self.fichamentira[0]:
                objeto = []
                for x in click:
                    contador += 1
                    if contador < 5:
                        objeto.append(x)
                    else:
                        objeto.append("izquierda")
                self.copiaclickiz.append(objeto)
                # copiaclick[5] = "izquierda"
                self.izquierda.append(click)
                self.fichamentira[0] = click[2]
                if jugador == 1:
                    self.fichas_jugador1.remove(click)
                elif jugador == 2:
                    self.fichas_jugador2.remove(click)
                elif jugador == 3:
                    self.fichas_jugador3.remove(click)
                elif jugador == 4:
                    self.fichas_jugador4.remove(click)
        print(str(self.fichamentira))
        cizquierda = ""
        cderecha = ""
        for x in self.izquierda:
            cizquierda = cizquierda + str(x)
        for x in self.derecha:
            cderecha = cderecha + str(x)
        # if click[2] == self.ultima_ficha_puesta[2] or click[3] == self.ultima_ficha_puesta[3] or click[2] == self.ultima_ficha_puesta[3] or click[3] == self.ultima_ficha_puesta[2]:
        #     self.ultima_ficha_puesta = click
        #     self.fichaseliminadas.append(click)
        #     print("FICHA CORRECTA")
        #     print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))
        #     if jugador == 1:
        #         self.fichas_jugador1.remove(click)
        #     elif jugador == 2:
        #         self.fichas_jugador2.remove(click)
        #     elif jugador == 3:
        #         self.fichas_jugador3.remove(click)
        #     elif jugador == 4:
        #         self.fichas_jugador4.remove(click)
        # else:
        #     print("FICHA INCORRECTA")
        #     print("ÚLTIMA FICHA PUESTA: " + str(self.ultima_ficha_puesta))

    def victoria(self):
        if len(self.fichas_jugador1) <= 0:
            print("GANÓ JUGADOR 1")
            self.victoria = 6
            return "si"
        elif len(self.fichas_jugador2) <= 0:
            print("GANÓ JUGADOR 2")
            self.victoria = 6
            return "si"
        elif len(self.fichas_jugador3) <= 0:
            print("GANÓ JUGADOR 3")
            self.victoria = 6
            return "si"
        elif len(self.fichas_jugador4) <= 0:
            print("GANÓ JUGADOR 4")
            self.victoria = 6
            return "si"
        else:
            return "no"
            
    # def puntuacion(self):
    #     if 