from random import randint
import pygame
from pygame.locals import RLEACCEL

from pioupiou import PioupiouEnnemi
class Ennemi(pygame.sprite.Sprite) :
    def __init__(self, vie, position: tuple) -> None:
        super(Ennemi, self).__init__()
        self._position = position
        self._vitesseFrappe = 12
        self._vie = vie
        self.timeTicks = 0
        self.surf = pygame.image.load("space_invader.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=position)
    
    def update(self, moveDirection) :
        self.rect.move_ip(-5 if moveDirection == "left" else 5, 0)

    def emitPioupiou(self) :
        self.pioupiou = PioupiouEnnemi((self.rect.x, self.rect.y), )
            

        