from random import choice
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
clock = pygame.time.Clock()
clock.tick(30)
font = pygame.font.SysFont("Comic Sans MC", 70)

class Label: #créer le texte cliquable
    def __init__(self, text, x, y): #initialisation du texte à cliquer par son contenu et position (x,y)
        self.x = x
        self.y = y
        self.set(text)
 
    def set(self, text):
        self.text = font.render(text, True, (229,229,229)) #texte + lissage + couleur
        w, h = self.text.get_size() #affectation hauteur + largeur du texte
        self.rect = pygame.Rect(self.x, self.y, w, h) #avoir la zone où on pourra cliquer sur le texe
        self.surface = pygame.Surface(screen.get_size())
        self.surface.blit(self.text, (self.x, self.y)) #affichage

lexit = Label("Exit", 285, 380)

class Party :    
    def __init__(self) -> None:
        self.level = 0
        self._joueur = Joueur()
        self._allSprites = pygame.sprite.Group()
        self._allSprites.add(self._joueur)
        self._listEnnemiPioupiou = pygame.sprite.Group()
        self._listJoueurPioupiou = pygame.sprite.Group()
        self.ENNEMIPIOUPIOU = pygame.USEREVENT + 1
        self.screen = pygame.display.set_mode([700, 700])
        self._score = 0
        
    def playRound(self) :
        #init et création des ennemis
        self._listEnnemis = pygame.sprite.Group()
        for y in range(4) :
            for x in range(6) :
                self._listEnnemis.add(Ennemi(40 + self.level * 5, (100 + 100 * x, 100 + y * 100)))
        self.update()
        pygame.time.set_timer(self.ENNEMIPIOUPIOU, 5000)

        ennemiMoveCounter = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 10 pixels, puis la même chose vers la gauche et ainsi de suite
        
    def CliqueSourisExit(lexit): #actions de la souris
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos() #position de la souris
            if lexit.rect.collidepoint(mx, my): #collision entre texte et souris
                pygame.quit()

    def Victory(): #écran victoire
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render('YOU WON!', True, (231, 193, 0))
        screen.blit(textsurface,(73,200))
        textscore = font.render('Score:', True, (255, 255, 255))
        screen.blit(textscore, (100, 600))
        screen.blit(self._score, (200, 600))

    def GameOver(): #écran défaite
        myfont = pygame.font.SysFont('Comic Sans MS', 100) #taille + style police du texte
        textsurface = myfont.render('GAME OVER', True, (255, 0, 0)) #texte + lissage + couleur
        screen.blit(textsurface,(50,200)) #affichage texte + position
        textscore = font.render('Score:', True, (255, 255, 255))
        screen.blit(textscore, (100, 600))

        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    running = False

                if event.type == self.ENNEMIPIOUPIOU :
                    choice(self._listEnnemis.sprites()).emitPioupiou()

            pressed_keys = pygame.key.get_pressed()
            self._joueur.update(pressed_keys)

            pariteEnnemiMove = (ennemiMoveCounter//5) % 2
            self._listEnnemis.update("right" if pariteEnnemiMove == 0 else "left")

            #gestion des colisions
            if pygame.sprite.spritecollideany(self._joueur, self._listEnnemiPioupiou) :
                self._joueur.vie -= 1
                running = False
            ennemiCollideDict = pygame.sprite.spritecollide(self._listJoueurPioupiou, self._listEnnemis, False, False)
            if ennemiCollideDict :
                for paire in ennemiCollideDict.items() :
                    paire[0].kill()
                    paire[1].kill()
                    del paire[0], paire[1]
                    self._score += 20
                if len(self._listEnnemis.sprites()) == 0 :
                    self.level += 1
                    running = False

            Party.screen.fill((0, 0, 0))
            self.update()
        
        self._listEnnemis.empty()
        return True if self._joueur.isAlive() else False

        if event.type == pygame.MOUSEBUTTONDOWN: #faire agir quand la souris clique
            CliqueSourisExit(lexit)
        screen.blit(lexit.surface, (0, 0))
    Victory() #A paramétrer entre Victory & GameOver
        
    def update(self) :
        #actualisation de l'affichage graphique
        for sprite in self._allSprites :
                Party.screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()


    def terminate(self) :
        pygame.quit()