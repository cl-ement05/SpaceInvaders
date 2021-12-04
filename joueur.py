import pygame

class Joueur(pygame.sprite.Sprite) : 
    def __init__(self) -> None:
        super(Joueur, self).__init__()
        self._vie = 3

    def isAlive(self) :
        return self._vie > 0

    def update(self, pressed_keys) :
        pass