import pygame

from constantes import *
from DIALOGOS import DialogueBox

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))

background = pygame.image.load(
    "assets/backgrounds/mancha.png"
).convert()

pygame.display.set_caption(
    "Don Quijote de la Mancha"
)

clock = pygame.time.Clock()

font = pygame.font.SysFont(
    "timesnewroman",
    32
)

dialogos = [

    "En un lugar de la Mancha...",
    
    "de cuyo nombre no quiero acordarme...",

    "no ha mucho tiempo que vivía un hidalgo...",

    "de los de lanza en astillero..."
]

dialogue_box = DialogueBox(
    font,
    dialogos
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

    pantalla.blit(background, (0,0))

    dialogue_box.draw(pantalla)

    pygame.display.update()

pygame.quit()