import pygame
from pygame.locals import RLEACCEL

class Joueur(pygame.sprite.Sprite) : 
    def __init__(self) -> None:
        super(Joueur, self).__init__()                     #permet d'initialiser la classe parente. Equivalent à super().__init__(self)
        self._vie = 3
        self.surf = pygame.image.load("IMAGENNEMI.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def isAlive(self) :
        return self._vie > 0

    def update(self, pressed_keys) :
        pass