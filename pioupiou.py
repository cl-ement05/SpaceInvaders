import pygame
from pygame.locals import RLEACCEL

class Pioupiou(pygame.sprite.Sprite):
    #définition des attributs : le paramètre position sera la position du joueur en couple de coordonnées
    #origin permet de savoir si le missile a été créé par le joueur ou par un ennemi
    #direction "up" ou "down" permet de savoir vers ou se dirige le missile
    def __init__(self, position):
        super(Pioupiou, self).__init__()      #permet d'initialiser la classe parente. Equivalent à super().__init__(self)
        self._position = position
    
class PioupiouEnnemi(Pioupiou) :
    def __init__(self, position):
        super().__init__(position)
        self.surf = pygame.image.load("IMAGE-mechantPIOUPIOU.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self) : #descends de haut en bas quoi jusqu'à BOUM
        self.rect.move_ip(0, -10)

class PioupiouJoueur(Pioupiou) :
    def __init__(self, position):
        super().__init__(position)
        self.surf = pygame.image.load("IMAGE-PIOUPIOU.jpg").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self) : #monte de bas en haut quoi jusqu'à BOUM
        self.rect.move_ip(0, 10) 