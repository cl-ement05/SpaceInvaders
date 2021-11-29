from random import randint
import pygame

class Ennemi(pygame.sprite.Sprite) :
    def __init__(self, vitesseFrappe, vie, surface, position = None) -> None:
        if position == None : position = (randint(0, 50), randint(0, 50))
        self._position = position
        self._vitesseFrappe = vitesseFrappe
        self._vie = vie
        self.surfc = surface

        