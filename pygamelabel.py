import pygame
defaultFont = pygame.font.SysFont("Comic Sans MC", 70)

class Label: #créer le texte cliquable
    def __init__(self, text, x, y, color = (229, 229, 229), font = defaultFont): #initialisation du texte à cliquer par son contenu et position (x,y)
        self._x = x
        self._y = y
        self._content = text
        self.font = font
        self.color = color

    def blit(self, display) :
        self.text = self.font.render(self._content, True, self.color) #texte + lissage + couleur
        w, h = self.text.get_size() #affectation hauteur + largeur du texte
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect(center = (self._x, self._y)) #avoir la zone où on pourra cliquer sur le texe
        self.surface.blit(self.text, (0, 0))
        display.blit(self.surface, self.rect)

    def CliqueSourisLabel(self): #actions de la souris
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos() #position de la souris
            if self.rect.collidepoint(mx, my): #collision entre texte et souris
                return True