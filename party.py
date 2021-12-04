from joueur import Joueur
from ennemi import Ennemi
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

def checkPygameInstallation() :
    global pygame
    try : 
        import pygame
    except ImportError :
        print("Erreur le module pygame est requis pour le bon fonctionnement de ce jeu")
        print("Voulez-vous que nous installions automatiquement ce module (Y/n)", end = " ")
        if input("") != "n" :
            print("Installation de pygame en cours...")
            import os
            command = ("python" if os.name == "nt" else "python3") + " -m pip install pygame"
            if not os.system(command) :
                print("Succès ! pygame a bien été installé")
                import pygame
            else : 
                print("Une erreur est survenue veuillez réessayer")
                exit()
        else : exit()
import pygame
pygame.init()

class Party :
    screen = pygame.display.set_mode([700, 700])
    
    def __init__(self) -> None:
        self.level = 1
        self._joueur = Joueur()
        self._listEnnemis = pygame.sprite.Group()
        
        
    def playRound(self) :
        ennemiMoveCounter = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 10 pixels, puis la même chose vers la gauche et ainsi de suite
        ennemi1 = Ennemi(40)
        ennemi1.update("left")
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    running = False

            pariteEnnemiMove = (ennemiMoveCounter//5) % 2
            self._listEnnemis.update("right" if pariteEnnemiMove == 0 else "left")
        
        return None if self._joueur.isAlive() else False
        

    def terminate(self) :
        pygame.quit()