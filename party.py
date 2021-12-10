from random import choice
from joueur import Joueur
from ennemi import Ennemi
from pioupiou import PioupiouEnnemi, PioupiouJoueur

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
pygame.display.set_caption("Space Invadors")
from pygamelabel import Label                     #on importe ici car pour initialiser des fonts, pygame.init() doit avoir tourné

class Party :    
    lexit = Label("Exit", 350, 500) #création bouton exit
    lplay = Label("Play", 350, 600) #création bouton play
    
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([700, 700])
        self.level = 0
        self._joueur = Joueur()
        self._allSprites = pygame.sprite.Group()
        self._allSprites.add(self._joueur)
        self._listEnnemiPioupiou = pygame.sprite.Group()
        self._listJoueurPioupiou = pygame.sprite.Group()
        self.ENNEMIPIOUPIOU = pygame.USEREVENT + 1
        self.ENNEMIDIRECTION = pygame.USEREVENT + 2
        self._score = 0
        
    def playRound(self) :
        #init et création des ennemis
        self._listEnnemis = pygame.sprite.Group()
        for y in range(4) :
            for x in range(6) :
                newEnnemy = Ennemi(40 + self.level * 5, (100 + 100 * x, 100 + y * 100))
                self._listEnnemis.add(newEnnemy)
                self._allSprites.add(newEnnemy)
        self.update()
        pygame.time.set_timer(self.ENNEMIPIOUPIOU, 5000)
        pygame.time.set_timer(self.ENNEMIDIRECTION, 2500)

        ennemiMoveCounter = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 10 pixels, puis la même chose vers la gauche et ainsi de suite

        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    return False

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
            ennemiCollideDict = pygame.sprite.groupcollide(self._listJoueurPioupiou, self._listEnnemis, False, False)
            if ennemiCollideDict :
                for paire in ennemiCollideDict.items() :
                    paire[0].kill()
                    paire[1].kill()
                    del paire[0], paire[1]
                    self._score += 20
                if len(self._listEnnemis.sprites()) == 0 :
                    self.level += 1
                    running = False

            self.screen.fill((0, 0, 0))
            self.update()
            ennemiMoveCounter += 1
        
        self._listEnnemis.empty()
        print(self._joueur.isAlive, self._joueur._vie)
        return True if self._joueur.isAlive() else False
        
    def update(self) :
        #actualisation de l'affichage graphique
        for sprite in self._allSprites :
            self.screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        clock.tick(30)


    def terminate(self) :
        pygame.quit()

    def Victory(self): #écran victoire
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render('YOU WON!', True, (231, 193, 0))
        self.screen.blit(textsurface,(73,200))
        textscore = myfont.render('Score:', True, (255, 255, 255))
        self.screen.blit(textscore, (100, 600))
        self.screen.blit(self._score, (200, 600))

    def GameOver(self): #écran défaite
        myfont = pygame.font.SysFont('Comic Sans MS', 100) #taille + style police du texte
        textsurface = myfont.render('GAME OVER', True, (255, 0, 0)) #texte + lissage + couleur
        self.screen.blit(textsurface,(50,200)) #affichage texte + position
        textscore = myfont.render('Score:', True, (255, 255, 255))
        self.screen.blit(textscore, (100, 600))

    def Welcome(self): #Ecran de démarrage
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        myfont2 = pygame.font.SysFont('Comic Sans MS', 75) #police + taille
        textWelcome = myfont.render('Welcome to', True, (255, 255, 255)) 
        textgame = myfont2.render('SPACE INVADORS', True, (255, 255, 255)) #texte + antialiasing + couleur
        self.screen.blit(textWelcome,(220,260)) 
        self.screen.blit(textgame, (10,300)) #texte à afficher + position
        return self.exitOrPlayMenu()

    def exitOrPlayMenu(self) :
        self.__class__.lexit.blit(self.screen)
        self.__class__.lplay.blit(self.screen)
        pygame.display.flip()
        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN: #faire agir quand la souris clique
                    if self.__class__.lplay.CliqueSourisLabel() : return True
                    if self.__class__.lexit.CliqueSourisLabel() : return False
            