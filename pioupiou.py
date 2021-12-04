import pygame

class Pioupiou(pygame.sprite.Sprite):
    #définition des attributs : le paramètre position sera la position du joueur en couple de coordonnées
    #origin permet de savoir si le missile a été créé par le joueur ou par un ennemi
    #direction "up" ou "down" permet de savoir vers ou se dirige le missile
    def __init__(self, position, origin: str, direction: str):
        self._damage = 20
        self._position = position
        self._origin = origin
        self._direction = direction

    #définition des méthodes des pioupiou
    def deplacement(self):
        if self._position != 0: #le bout de la map
            self._position[1] +=1 #pas sûr là mais ça doit juste monter le y de 1
    
class PioupiouEnnemi(Pioupiou) :
    def __init__(self, position, origin: str, direction: str):
        super().__init__(position, origin, direction)

class PioupiouJoueur(Pioupiou) :
    def __init__(self, position, origin: str, direction: str):
        super().__init__(position, origin, direction)