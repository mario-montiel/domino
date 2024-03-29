import pygame, sys
from pygame.locals import *
from domino.juego import Juego
from database.db import Conexion
import random

class MAINjuego:
	def popo(self):
		juego = Juego()
		pygame.init()
		ventanta = pygame.display.set_mode((1350,700))
		pygame.display.set_caption("El dominó mamalón")
		fichas = []
		total_fichas = []
		tiempo = 0

		fuenteconexion = pygame.font.SysFont("Arial", 30)
		Mi_imagen = pygame.image.load("imagenes_domino/main_menu.jpg")
		Mi_imagen2  = pygame.image.load("imagenes_domino/register.jpg")
		Mi_imagen3 = pygame.image.load("domino/board2.jpg")
		stabton = pygame.Rect(550,460,282,50)
		maus = pygame.Rect(0, 0, 25, 25)
		pantalla = 1
		btoncomenzar2 = pygame.Rect(550000,460000,282,50)

		input_box = pygame.Rect(100,100, 140, 32)
		input_box2 = pygame.Rect(100,100, 140, 32)
		input_box3 = pygame.Rect(100,100, 140, 32)
		input_box4 = pygame.Rect(100,100, 140, 32)
		color_inactive = pygame.Color(228,201,0)
		color_active = pygame.Color(255,240,133)
		btonsaliendo = pygame.Rect(550,598,282,50)
		color = color_inactive
		color2 = color_inactive
		color3 = color_inactive
		color4 = color_inactive
		active2 = False
		active3 = False
		active4 = False
		active = False
		text = ''
		text2 = ''
		text3 = ''
		text4 = ''
		done = False
		ganar = "no"
		klado = "i"
		veces = 1

		# turno = 0
		# fichaaguardar = None
		clock = pygame.time.Clock()

		rand = random.randint(1,3)
		if int(rand) == 1:
			pygame.mixer.music.load('mp3/soundfile_1.mp3')
			pygame.mixer.music.play(-1)
			pygame.mixer.init()
		elif int(rand) == 2:
			pygame.mixer.music.load('mp3/soundfile_2.mp3')
			pygame.mixer.music.play(-1)
			pygame.mixer.init()
		elif int(rand) == 3:
			pygame.mixer.music.load('mp3/soundfile_3.mp3')
			pygame.mixer.music.play(-1)
			pygame.mixer.init()

		while True:
			clock.tick(30)
			maus.left, maus.top = pygame.mouse.get_pos()
			db = Conexion()
			if pantalla == 1:
				ventanta.blit(Mi_imagen, (0, 0))
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if maus.colliderect(stabton):
							stabton = pygame.Rect(100000,100000, 670, 50)
							btonsaliendo = pygame.Rect(550000000,46000000,282,50)
							btoncomenzar2 = pygame.Rect(550,610,282,50)
							pantalla = 2
						elif maus.colliderect(btonsaliendo):
							pygame.quit()
							sys.exit()
			elif pantalla == 2:
				ventanta.blit(Mi_imagen2, (0, 0))
				font = pygame.font.Font(None, 32)
				input_box = pygame.Rect(520, 260, 340, 32)
				input_box2 = pygame.Rect(520,335, 340, 32)
				input_box3 = pygame.Rect(520,410, 340, 32)
				input_box4 = pygame.Rect(520,485, 340, 32)
				try:
					juego.mula = db.obtener_mula()
					fichas = random.sample(db.database(1), k=28)
					total_fichas = random.sample(db.database(1), k = 28)
				except:
					eltexto = fuenteconexion.render("!! NO SE ENCONTRÓ NINGUNA BASE DE DATOS !!", 0, (233,233,87))
					ventanta.blit(eltexto,(400,50))

				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if input_box.collidepoint(event.pos):
							active = not active
							active2 = False
							active3 = False
							active4 = False
						elif input_box2.collidepoint(event.pos):
							active2 = not active2
							active = False
							active3 = False
							active4 = False
						elif input_box3.collidepoint(event.pos):
							active3 = not active3
							active = False
							active2 = False
							active4 = False
						elif input_box4.collidepoint(event.pos):
							active4 = not active4
							active = False
							active2 = False
							active3 = False
						elif maus.colliderect(btoncomenzar2):
							nombre_jugadores = []
							nombre_jugadores.append(text)
							nombre_jugadores.append(text2)
							nombre_jugadores.append(text3)
							nombre_jugadores.append(text4)
							juego.fichas = set(fichas)
							juego.repartir_fichas(1, total_fichas)
							juego.repartir_fichas(2, total_fichas)
							juego.repartir_fichas(3, total_fichas)
							juego.repartir_fichas(4, total_fichas)
							try:
								db.ingresar_jugadores(nombre_jugadores)
								db.asignar_fichas_db(2, juego.fichas_jugador1, juego.fichas_jugador2, juego.fichas_jugador3, juego.fichas_jugador4, fichas)
								turno = juego.poner_mula(total_fichas)
								btoncomenzar2 = pygame.Rect(550000,460000,282,50)
								pantalla = 3
								input_box = pygame.Rect(520000, 260000, 340, 32)
								input_box2 = pygame.Rect(520000,335000, 340, 32)
								input_box3 = pygame.Rect(520000,410000, 340, 32)
								input_box4 = pygame.Rect(520000,485000, 340, 32)
							except:
								print("error")
							# 
						else:
							active = False
							active2 = False
							active3 = False
							active4 = False
						color = color_active if active else color_inactive
						color2 = color_active if active2 else color_inactive
						color3 = color_active if active3 else color_inactive
						color4 = color_active if active4 else color_inactive
					elif event.type == pygame.KEYDOWN:
						if active:
							if event.key == pygame.K_RETURN:
								print(text)
								text = ''
							elif event.key == pygame.K_BACKSPACE:
								text = text[:-1]
							else:
								text += event.unicode
						if active2:
							if event.key == pygame.K_RETURN:
								print(text2)
								text2 = ''
							elif event.key == pygame.K_BACKSPACE:
								text2 = text2[:-1]
							else:
								text2 += event.unicode
						if active3:
							if event.key == pygame.K_RETURN:
								print(text3)
								text3 = ''
							elif event.key == pygame.K_BACKSPACE:
								text3 = text3[:-1]
							else:
								text3 += event.unicode
						if active4:
							if event.key == pygame.K_RETURN:
								print(text4)
								text4 = ''
							elif event.key == pygame.K_BACKSPACE:
								text4 = text4[:-1]
							else:
								text4 += event.unicode

				txt_surface = font.render(text, True, color)
				width = max(500, txt_surface.get_width()+10)
				input_box.w = width
				ventanta.blit(txt_surface, (input_box.x+5, input_box.y+5))
				pygame.draw.rect(ventanta, color, input_box, 2)

				txt_surface2 = font.render(text2, True, color2)
				width = max(500, txt_surface2.get_width()+10)
				input_box2.w = width
				ventanta.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
				pygame.draw.rect(ventanta, color2, input_box2, 2)

				txt_surface3 = font.render(text3, True, color3)
				width = max(500, txt_surface3.get_width()+10)
				input_box3.w = width
				ventanta.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
				pygame.draw.rect(ventanta, color3, input_box3, 2)

				txt_surface4 = font.render(text4, True, color4)
				width = max(500, txt_surface4.get_width()+10)
				input_box4.w = width
				ventanta.blit(txt_surface4, (input_box4.x+5, input_box4.y+5))
				pygame.draw.rect(ventanta, color4, input_box4, 2)
			elif pantalla == 3:
				timer_resolution = pygame.TIMER_RESOLUTION
				cuadroizquierdo = pygame.Rect(500,100,150,50)
				tiempo += timer_resolution
				ventanta.blit(Mi_imagen3, (0, 0))
				# botón
				btonreiniciartodoalavrga = pygame.Rect(1150,600,150,50)
				pygame.draw.rect(ventanta, (235,192,0), btonreiniciartodoalavrga)
				# texto del botón
				fuente = pygame.font.Font(None, 30)
				untexto = fuente.render("Reiniciar", 0, (0,0,0))
				ventanta.blit(untexto, (1177,615))

				todosloscuadros = []
				contadordefichas = 0
				if turno == 1:
					jugador = pygame.image.load("imagenes_domino/Jugador-1.png")
					ventanta.blit(jugador, (0, 0))
					fichas = juego.fichas_jugador1
					posicionesx = 600
					for x in fichas:
						contadordefichas += 1
						fichaj1 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
						ventanta.blit(fichaj1, (posicionesx, 0))
						cuadro = pygame.Rect(posicionesx, 2, 60, 50)
						cuadro2 = pygame.Rect(posicionesx, 57, 60, 50)
						todosloscuadros.append(cuadro)
						todosloscuadros.append(cuadro2)
						posicionesx += 60
					if ganar == "si":
						fuente = pygame.font.Font(None,50)
						eltexto1 = fuente.render("ganó el jugador 4!!", 0, (233,233,87))
						ventanta.blit(eltexto1,(550,400))
				elif turno == 2:
					jugador = pygame.image.load("imagenes_domino/Jugador-2.png")
					ventanta.blit(jugador, (0, 0))
					fichas = juego.fichas_jugador2
					posicionesx = 600
					for x in fichas:
						contadordefichas += 1
						fichaj1 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
						ventanta.blit(fichaj1, (posicionesx, 0))
						cuadro = pygame.Rect(posicionesx, 2, 60, 50)
						cuadro2 = pygame.Rect(posicionesx, 57, 60, 50)
						todosloscuadros.append(cuadro)
						todosloscuadros.append(cuadro2)
						posicionesx += 60
					if ganar == "si":
						fuente = pygame.font.Font(None,50)
						eltexto1 = fuente.render("ganó el jugador 1!!", 0, (233,233,87))
						ventanta.blit(eltexto1,(550,400))
				elif turno == 3:
					jugador = pygame.image.load("imagenes_domino/Jugador-3.png")
					ventanta.blit(jugador, (0, 0))
					fichas = juego.fichas_jugador3
					posicionesx = 600
					for x in fichas:
						contadordefichas += 1
						fichaj1 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
						ventanta.blit(fichaj1, (posicionesx, 0))
						cuadro = pygame.Rect(posicionesx, 2, 60, 50)
						cuadro2 = pygame.Rect(posicionesx, 57, 60, 50)
						todosloscuadros.append(cuadro)
						todosloscuadros.append(cuadro2)
						posicionesx += 60
					if ganar == "si":
						fuente = pygame.font.Font(None,50)
						eltexto1 = fuente.render("ganó el jugador 2!!", 0, (233,233,87))
						ventanta.blit(eltexto1,(550,400))
				elif turno == 4:
					jugador = pygame.image.load("imagenes_domino/Jugador-4.png")
					ventanta.blit(jugador, (0, 0))
					fichas = juego.fichas_jugador4
					posicionesx = 600
					for x in fichas:
						contadordefichas += 1
						fichaj1 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
						ventanta.blit(fichaj1, (posicionesx, 0))
						cuadro = pygame.Rect(posicionesx, 2, 60, 50)
						cuadro2 = pygame.Rect(posicionesx, 57, 60, 50)
						todosloscuadros.append(cuadro)
						todosloscuadros.append(cuadro2)
						posicionesx += 60
					if ganar == "si":
						fuente = pygame.font.Font(None,50)
						eltexto1 = fuente.render("ganó el jugador 3!!", 0, (233,233,87))
						ventanta.blit(eltexto1,(550,400))
				posicionesx = 700
				# yaponidas = juego.fichaseliminadas
				# for x in yaponidas:
				# 	ficha2 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
				# 	ventanta.blit(ficha2, (posicionesx, 200))
				# 	posicionesx += 20
				izquierda = juego.izquierda
				derecha = juego.derecha
				izquierda2 = juego.copiaclickiz
				derecha2 = juego.copiaclickde
				ficha2 = pygame.image.load("domino/piezas_domino/28.jpg")
				ficha2 = pygame.transform.scale(ficha2,(30,60))
				ficha2 = pygame.transform.rotate(ficha2, 90)
				ventanta.blit(ficha2, (posicionesx, 200))
				for x in izquierda:
					posicionesx -= 60
					ficha2 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
					ficha2 = pygame.transform.scale(ficha2,(30,60))
					for y in izquierda2:
						if y[0] == x[0]:
							ficha2 = pygame.transform.rotate(ficha2, 90)
					for y in derecha2:
						if y[0] == x[0]:
							ficha2 = pygame.transform.rotate(ficha2, -90)
					ventanta.blit(ficha2, (posicionesx, 200))
				posicionesx = 700
				for x in derecha:
					posicionesx += 60
					ficha2 = pygame.image.load("domino/piezas_domino/" + str(x[0]) + ".jpg")
					ficha2 = pygame.transform.scale(ficha2,(30,60))
					for y in izquierda2:
						if y[0] == x[0]:
							ficha2 = pygame.transform.rotate(ficha2, 90)
					for y in derecha2:
						if y[0] == x[0]:
							ficha2 = pygame.transform.rotate(ficha2, -90)
					ventanta.blit(ficha2, (posicionesx, 200))
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.KEYDOWN:
						if event.key == K_LEFT:
							klado = "i"
						elif event.key == K_RIGHT:
							klado = "d"
					elif event.type == MOUSEBUTTONDOWN:
						if(tiempo > 500):
							veces = 1
							tiempo = 0
						if veces == 1:
							veces = 0
							print(contadordefichas)
							for x in todosloscuadros:
								if maus.colliderect(x):
									if maus.left > 600 and maus.left < 660:
										fichaaguardar = 0
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[0], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[0], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[0], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[0], turno, klado)
									elif maus.left < 720 and maus.left > 660:
										fichaaguardar = 1
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[1], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[1], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[1], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[1], turno, klado)
									elif maus.left < 780 and maus.left > 720:
										fichaaguardar = 2
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[2], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[2], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[2], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[2], turno, klado)
									elif maus.left < 840 and maus.left > 780:
										fichaaguardar = 3
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[3], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[3], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[3], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[3], turno, klado)
									elif maus.left < 900 and maus.left > 84:
										fichaaguardar = 4
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[4], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[4], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[4], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[4], turno, klado)
									elif maus.left < 960 and maus.left > 900:
										fichaaguardar = 5
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[5], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[5], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[5], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[5], turno, klado)
									elif maus.left > 960 and maus.left < 1020:
										fichaaguardar = 6
										if turno == 1:
											juego.poner_ficha(juego.fichas_jugador1[6], turno, klado)
										elif turno == 2:
											juego.poner_ficha(juego.fichas_jugador2[6], turno, klado)
										elif turno == 3:
											juego.poner_ficha(juego.fichas_jugador3[6], turno, klado)
										elif turno == 4:
											juego.poner_ficha(juego.fichas_jugador4[6], turno, klado)
								elif maus.colliderect(btonreiniciartodoalavrga):
									juego.reiniciartodoalavrga()
									btonreiniciartodoalavrga = pygame.Rect(115000,6000000,150,50)
									pantalla = 1
									todosloscuadros = []
									stabton = pygame.Rect(550,460,282,50)
									btonsaliendo = pygame.Rect(550,598,282,50)
									text = ''
									text2 = ''
									text3 = ''
									text4 = ''
									self.popo()
								ganar = juego.victoria()
							turno = turno + 1
							if turno == 5:
								turno = 1
			pygame.display.update()
juego2 = MAINjuego()
juego2.popo()