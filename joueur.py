import pygame
from pygame.locals import (
    RLEACCEL,
    K_LEFT,
    K_RIGHT,
    K_SPACE
)

from pioupiou import PioupiouJoueur
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Joueur(pygame.sprite.Sprite) : 
    def __init__(self) -> None:
        super(Joueur, self).__init__()#permet d'initialiser la classe parente. Equivalent à super().__init__(self)
        self._vie = 3
        self.surf = pygame.image.load("images/joueur.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(350,600))

    def isAlive(self) :
        return self._vie > 0

    def diminuerVie(self, value: int) : self._vie -= value

    def update(self, pressed_keys):#les touches quand ça joue
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-8, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(8, 0)
        if pressed_keys[K_SPACE] :
            return True

        #ne pas sortir de la map
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def instantiatePioupiou(self) :
        return PioupiouJoueur((self.rect.centerx, self.rect.top))