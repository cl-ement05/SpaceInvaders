class Pioupiou:
    #définition des attributs : le paramètre position sera la position du joueur en couple de coordonnées
    def __init__(self, position):
        _damage = 20
        _position = position

    #définition des méthodes des pioupiou
    def deplacement(self):
        if self._position != 0: #le bout de la map
            self._position[1] +=1 #pas sûr là mais ça doit juste monter le y de 1

    def kboum(self):#quand ça touche un ennemi
        del self
    