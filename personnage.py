import pygame

class Peronnage(pygame.sprite.Sprite) :
    def __init__(self) -> None:
        pass

    def isAlive(self) :
        return self._vie > 0