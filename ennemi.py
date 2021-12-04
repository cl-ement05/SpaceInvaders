from random import randint
import pygame
from pygame.locals import RLEACCEL

from pioupiou import Pioupiou
class Ennemi(pygame.sprite.Sprite) :
    def __init__(self, vie, position = None) -> None:
        if position == None : position = (randint(0, 50), randint(0, 50))
        super(Ennemi, self).__init__()
        self._position = position
        self._vitesseFrappe = 12
        self._vie = vie
        self.timeTicks = 0
        self.surfc = pygame.image.load("space_invader.jpg").convert()
        self.surfc.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surfc.get_rect()
    
    def update(self, moveDirection) :
        self.rect.move_ip(-5 if moveDirection == "left" else 5, 0)
        if (self.timeTicks - pygame.time.get_ticks()) % 12 :             #-> lancer un missile tt les 12sec
            self.pioupiou = Pioupiou((self.rect.x, self.rect.y))
            

        