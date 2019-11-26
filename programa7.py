import pygame, sys
from pygame.locals import *

pygame.init()
ventanta = pygame.display.set_mode((1350,700))
pygame.display.set_caption("El dominó mamalón")

Mi_imagen = pygame.image.load("domino/board3.jpg")
Mi_imagen2  = pygame.image.load("domino/board2.jpg")
stabton = pygame.Rect(370,540,670,50)
maus = pygame.Rect(0, 0, 25, 25)
pantalla = 1

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
		input_box1 = pygame.Rect(100,100,140,32)
		color_inactive = pygame.Color('lightskyblue3')
		color_active = pygame.Color('dodgerblue2')
		color = color_inactive
		active = False
		text = ''
		done = False
		font = pygame.font.Font(None, 32)

		ventanta.fill((30, 30, 30))
		txt_surface = font.render(text, True, color)
		width = max(200, txt_surface.get_width()+10)
		input_box1.w = width
		pantalla.blit(txt_surface, (input_box1.x+5, input_box1.y+5))
		pygame.draw.rect(screen, color, input_box1, 2)

		ventanta.blit(Mi_imagen2, (0, 0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_box1.collidepoint(event.pos):
					active = not active
				else:
					active = False
				color = color_active if active else color_inactive
			elif event.type == pygame.KEYDOWN:
				if active:
					if event.key == pygame.K_RETURN:
						print(text)
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode
	pygame.display.update()