import pygame

from constantes import *


class DialogueBox:

    def __init__(self, textos):

        self.textos = textos
        self.index = 0

        self.font_nombre = pygame.font.SysFont(
            "timesnewroman",
            36,
            bold=True
        )

        self.font_texto = pygame.font.SysFont(
            "timesnewroman",
            32
        )

    def next_text(self):

        if self.index < len(self.textos) - 1:
            self.index += 1

    def draw(self, pantalla):

        caja = pygame.Rect(
            40,
            500,
            1200,
            180
        )

        pygame.draw.rect(
            pantalla,
            COLOR_CAJA,
            caja
        )

        pygame.draw.rect(
            pantalla,
            (255, 255, 255),
            caja,
            3
        )

        nombre = self.textos[self.index][0]
        frase = self.textos[self.index][1]

        nombre_surface = self.font_nombre.render(
            nombre,
            True,
            (255, 255, 0)
        )

        texto_surface = self.font_texto.render(
            frase,
            True,
            COLOR_TEXTO
        )

        pantalla.blit(
            nombre_surface,
            (70, 520)
        )

        pantalla.blit(
            texto_surface,
            (70, 560)
        )
capitulo_1 = [

    (
        "Narrador",
        "Al amanecer, Don Quijote abandonó su aldea."
    ),

    (
        "Narrador",
        "Rocinante avanzaba lentamente por los caminos de La Mancha."
    ),

    (
        "Don Quijote",
        "Por fin comienza mi aventura."
    ),

    (
        "Don Quijote",
        "Mi nombre será conocido en todo el reino."
    )

]

capitulo_2 = [

    (
        "Narrador",
        "Tras horas de viaje, divisó una venta a lo lejos."
    ),

    (
        "Don Quijote",
        "¡Un magnífico castillo!"
    ),

    (
        "Narrador",
        "La realidad era bastante menos impresionante."
    )

]

capitulo_3_alt = [

    (
        "Narrador",
        "La historia tomó un rumbo inesperado."
    ),

    (
        "Don Quijote",
        "Mi aventura aún no ha terminado."
    )

]

capitulo_4_alt = [

    (
        "Narrador",
        "Comienza la última aventura del caballero."
    )

]

CAPITULOS = {
    "cap1": capitulo_1,
    "cap2": capitulo_2,
    "cap3_alt": capitulo_3_alt,
    "cap4_alt": capitulo_4_alt,
}