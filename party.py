from joueur import Joueur
from ennemi import Ennemi
from pioupiou import PioupiouEnnemi, PioupiouJoueur
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
        self._allSprites = pygame.sprite.Group()
        self._allSprites.add(self._joueur)        
        
    def playRound(self) :
        ennemiMoveCounter = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 10 pixels, puis la même chose vers la gauche et ainsi de suite
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    running = False

            pressed_keys = pygame.key.get_pressed()
            self._joueur.update(pressed_keys)

            pariteEnnemiMove = (ennemiMoveCounter//5) % 2
            self._listEnnemis.update("right" if pariteEnnemiMove == 0 else "left")

            #gestion des colisions
            if pygame.sprite.spritecollideany(PioupiouEnnemi, self._joueur) :
                self._joueur.vie -= 1
                running = False
            ennemiCollidePioupiou = pygame.sprite.spritecollideany(PioupiouJoueur, self._listEnnemis)
            if ennemiCollidePioupiou :
                ennemiCollidePioupiou.kill()
                del ennemiCollidePioupiou

            Party.screen.fill((0, 0, 0))
            #actualisation de l'affichage graphique
            for sprite in self._allSprites :
                Party.screen.blit(sprite.surf, sprite.rect)
            pygame.display.flip()
        
        return None if self._joueur.isAlive() else False
        

    def terminate(self) :
        pygame.quit()