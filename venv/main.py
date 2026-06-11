import pygame

from constantes import *

from DIALOGOS import (
    DialogueBox,
    CAPITULOS,
    ORDEN_NORMAL,
    ORDEN_ALTERNATIVO
)

pygame.init()

pantalla = pygame.display.set_mode(
    (ANCHO, ALTO)
)

background = pygame.image.load(
    "/home/wewo/Escritorio/proyecto_inmersivo/juego_don_quijote/venv/assets/backgrounds/mancha.jpg"
).convert()

pygame.display.set_caption(
    "Don Quijote de la Mancha"
)

clock = pygame.time.Clock()

font_opciones = pygame.font.SysFont(
    "timesnewroman",
    28
)

indice_capitulo = 0

orden_actual = [
    "cap1",
    "cap2"
]

mostrar_decision = True
print("DECISION ACTIVADA")

opcion_seleccionada = 0

opciones = [
    "Ayudar al campesino",
    "Continuar el viaje"
]

dialogue_box = DialogueBox(
    CAPITULOS[
        orden_actual[indice_capitulo]
    ]
)

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if mostrar_decision:

                if event.key == pygame.K_UP:

                    opcion_seleccionada -= 1

                    if opcion_seleccionada < 0:
                        opcion_seleccionada = len(opciones) - 1

                elif event.key == pygame.K_DOWN:

                    opcion_seleccionada += 1

                    if opcion_seleccionada >= len(opciones):
                        opcion_seleccionada = 0

                elif event.key == pygame.K_RETURN:
                    print("ENTER PRESIONADO")

                    if opcion_seleccionada == 0:

                        orden_actual = ORDEN_ALTERNATIVO

                        indice_capitulo = 2

                    else:

                        orden_actual = ORDEN_NORMAL

                        indice_capitulo = 2

                    dialogue_box.textos = (
                        CAPITULOS[
                            orden_actual[
                                indice_capitulo
                            ]
                        ]
                    )

                    dialogue_box.index = 0

                    mostrar_decision = False

            elif event.key == pygame.K_SPACE:

                if dialogue_box.index < len(dialogue_box.textos) - 1:

                    dialogue_box.next_text()

                else:

                    if (
                        indice_capitulo ==
                        len(orden_actual) - 1
                    ):

                        pass

                    elif indice_capitulo == 1:
                        mostrar_decision = True

                    else:

                        indice_capitulo += 1

                        dialogue_box.textos = (
                            CAPITULOS[
                                orden_actual[
                                    indice_capitulo
                                ]
                            ]
                        )

                        dialogue_box.index = 0

    pantalla.blit(
        background,
        (0, 0)
    )

    dialogue_box.draw(
        pantalla
    )

    if mostrar_decision:
        print("ESTOY EN LA DECISION")
        titulo = font_opciones.render(
            "¿Que hara Don Quijote?",
            True,
            (255, 255, 255)
        )

        pantalla.blit(
            titulo,
            (80, 250)
        )

        for i, opcion in enumerate(opciones):

            if i == opcion_seleccionada:

                texto = "► " + opcion

            else:

                texto = "  " + opcion

            texto_surface = font_opciones.render(
                texto,
                True,
                (255, 255, 255)
            )

            pantalla.blit(
                texto_surface,
                (80, 300 + i * 40)
            )

    pygame.display.update()

pygame.quit()