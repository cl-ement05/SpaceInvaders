from personnage import Personnage
from ennemi import Ennemi
from pygameLogic import Pygame

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

class Party :
    def __init__(self) -> None:
        self._pygame = Pygame()
        self.level = 1
        self._joueur = Personnage()
        self._listEnnemis = list()
        
    def playRound(self) :
        #tant que le joueur est en vie, on continue le round
        while self._joueur.isAlive() :
            #on bouge les ennemis
            self._pygame.moveEnnemies()

        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    self.running = False

        pygame.quit()

    def terminate(self) :
        pass