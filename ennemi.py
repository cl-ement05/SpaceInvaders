from random import randint

class Ennemi :
    def __init__(self, vitesseFrappe, vie, position = None) -> None:
        if position == None : position = (randint(0, 50), randint(0, 50))
        
        self._position = position
        self._vitesseFrappe = vitesseFrappe
        self._vie = vie
        