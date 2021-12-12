import pygame
from pygame.locals import RLEACCEL

from pioupiou import PioupiouEnnemi
class Ennemi(pygame.sprite.Sprite) :
    def __init__(self, position: tuple) -> None:
        super(Ennemi, self).__init__()
        self._position = position
        self.surf = pygame.image.load("space_invader.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
    
    def update(self, moveDirection) :
        self.rect.move_ip(-4 if moveDirection == "left" else 4, 0)

    def emitPioupiou(self) :
        self.pioupiou = PioupiouEnnemi((self.rect.centerx, self.rect.bottom))
        return self.pioupiou

class BigBoss(Ennemi) :
    def __init__(self, position: tuple) -> None:
        super().__init__(position)
        self.surf = pygame.image.load("bigboss2.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
        self._vie = 10
    
    def retirerVie(self, malus) : self._vie -= malus
    def isAlive(self) : return self._vie > 0

    def update(self, moveDirection) :
        self.rect.move_ip(-8 if moveDirection == "left" else 8, 0)