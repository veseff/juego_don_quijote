import pygame

from constantes import *

class DialogueBox:

    def __init__(self, font, textos):

        self.font = font

        self.textos = textos

        self.index = 0

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
            (255,255,255),
            caja,
            3
        )

        texto = self.font.render(
            self.textos[self.index],
            True,
            COLOR_TEXTO
        )

        pantalla.blit(
            texto,
            (70,550)
        )