import pygame

pygame.init()

ancho = 800
alto = 600

pantalla = pygame.display.set_mode ((ancho,alto))

pygame.display.set_caption("Don Quijote de la Mancha")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()