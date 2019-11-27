import pygame, sys
from pygame.locals import *
import random

pygame.init()
ventanta = pygame.display.set_mode((1350,700))
pygame.display.set_caption("El dominó mamalón")

Mi_imagen = pygame.image.load("imagenes_domino/main_menu.jpg")
Mi_imagen2  = pygame.image.load("imagenes_domino/register.jpg")
stabton = pygame.Rect(550,460,282,50)
maus = pygame.Rect(0, 0, 25, 25)
pantalla = 1

input_box = pygame.Rect(100,100, 140, 32)
input_box2 = pygame.Rect(100,100, 140, 32)
input_box3 = pygame.Rect(100,100, 140, 32)
input_box4 = pygame.Rect(100,100, 140, 32)
color_inactive = pygame.Color(228,201,0)
color_active = pygame.Color(255,240,133)
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
	maus.left, maus.top = pygame.mouse.get_pos()
	if pantalla == 1:
		ventanta.blit(Mi_imagen, (0, 0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if maus.colliderect(stabton):
					stabton = pygame.Rect(100000,100000, 670, 50)
					pantalla = 2
	elif pantalla == 2:
		ventanta.blit(Mi_imagen2, (0, 0))
		font = pygame.font.Font(None, 32)
		input_box = pygame.Rect(520, 260, 340, 32)
		input_box2 = pygame.Rect(520,335, 340, 32)
		input_box3 = pygame.Rect(520,410, 340, 32)
		input_box4 = pygame.Rect(520,485, 340, 32)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if input_box.collidepoint(event.pos):
					active = not active
				elif input_box2.collidepoint(event.pos):
					active2 = not active2
				elif input_box3.collidepoint(event.pos):
					active3 = not active3
				elif input_box4.collidepoint(event.pos):
					active4 = not active4
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
	pygame.display.update()