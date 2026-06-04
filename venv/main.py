import pygame

from constantes import *
from DIALOGOS import DialogueBox
from DIALOGOS import CAPITULOS

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))

background = pygame.image.load(
    "/home/wewo/Escritorio/proyecto_inmersivo/juego_don_quijote/venv/assets/backgrounds/mancha.jpg"
).convert()

pygame.display.set_caption(
    "Don Quijote de la Mancha"
)

clock = pygame.time.Clock()

dialogue_box = DialogueBox(
    CAPITULOS["cap1"]
)

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                dialogue_box.next_text()

    pantalla.blit(background, (0, 0))

    dialogue_box.draw(pantalla)

    pygame.display.update()

pygame.quit()