import pygame

pygame.init()

ancho = 800
alto = 600

pantalla = pygame.display.set_mode ((ancho,alto))

reloj = pygame.time.Clock()

FPS = 60

pygame.display.set_caption("Don Quijote de la Mancha")

run = True

while run:
    reloj.tick(FPS)
    pantalla.fill((30,30,30))
    pygame.draw.rect(
        pantalla,
        (225,225,0),
        (100,100,50,50)
    )
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()