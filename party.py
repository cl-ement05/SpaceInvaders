from random import choice
from joueur import Joueur
from ennemi import BigBoss, Ennemi

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
        self._listEnnemiPioupiou = pygame.sprite.Group()
        self._joueurPioupiou = self._joueur.instantiatePioupiou()
        self.ENNEMIPIOUPIOU = pygame.USEREVENT + 1
        self.ENNEMIDIRECTION = pygame.USEREVENT + 2
        self._score = 0
        
    def playRound(self) :
        print("ROUND", self.level + 1)
        self._allSprites.add(self._joueur)

        #init et création des ennemis
        #si on atteint le niveau 20, big boss
        if self.level == 19 :
            self._listEnnemis.add(BigBoss(350, 250))
            bigboss = True
        else :
            bigboss = False
            self._listEnnemis = pygame.sprite.Group()
            for y in range(4) :
                for x in range(6) :
                    newEnnemy = Ennemi((50 + 100 * x, 100 + y * 100))
                    self._listEnnemis.add(newEnnemy)
                    self._allSprites.add(newEnnemy)
        self.update()

        #Déclaration des events custom
        pygame.time.set_timer(self.ENNEMIPIOUPIOU, 4000 - 500 * self.level)
        pygame.time.set_timer(self.ENNEMIDIRECTION, 1000)                       #permet de faire le va et vient des ennemis ; toutes les secondes : changement de direction

        ennemiMoveDirection = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 4 pixels, puis la même chose vers la gauche et ainsi de suite

        #BOUCLE DE JEU
        running = True
        while running :
            #GESTION DES EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    return "quit"

                if event.type == self.ENNEMIPIOUPIOU :
                    newPioupiou = choice(self._listEnnemis.sprites()).emitPioupiou()      #on choisit un ennemi au hasard et on lui fait tirer un missile qu'on ajoute à la liste des sprites
                    self._allSprites.add(newPioupiou)
                    self._listEnnemiPioupiou.add(newPioupiou)

                if event.type == self.ENNEMIDIRECTION :
                    ennemiMoveDirection += 1

            #GESTION DES INPUTS
            pressed_keys = pygame.key.get_pressed()
            if self._joueur.update(pressed_keys) :                #cf documentation
                if not self._joueurPioupiou.alive() :                   #on vérifie que aucun missile n'est "en cours"    
                    newPioupiou = self._joueur.instantiatePioupiou()
                    self._allSprites.add(newPioupiou)
                    self._joueurPioupiou = newPioupiou

            #MISE A JOUR DES POSITIONS
            if not bigboss : self._listEnnemis.update("right" if ennemiMoveDirection % 2 == 0 else "left")       #nombre pair -> les ennemis vont vers la droite sinon ils vont à gauche
            for pioupiou in self._listEnnemiPioupiou :
                pioupiou.update()
            if self._joueurPioupiou.alive() : self._joueurPioupiou.update()

            #GESTION DES COLLISIONS
            collideJoueurPioupiouE = pygame.sprite.spritecollideany(self._joueur, self._listEnnemiPioupiou)   #=sprite d'un pioupiou ennemi s'il touche le joueur
            if collideJoueurPioupiouE :
                self._joueur.diminuerVie(1)
                collideJoueurPioupiouE.kill()
                running = False
            
            ennemiCollide = pygame.sprite.spritecollideany(self._joueurPioupiou, self._listEnnemis)   #on récupère l'ennemi qui a été touché par le missile du joueur
            if ennemiCollide :
                print(self._joueurPioupiou, ennemiCollide)
                if not bigboss :               #si pas en mode bigboss -> le missile du joueur tue l'ennemi instantanément
                    ennemiCollide.kill()
                    self._joueurPioupiou.kill()
                else : 
                    ennemiCollide.retirerVie(1)                               #sinon on retire une vie au bigboss (il faut 10 missiles pour le tuer)
                    if not ennemiCollide.isAlive() : ennemiCollide.kill() 
                self._score += 10
                if len(self._listEnnemis.sprites()) == 0 :     
                    self.level += 1
                    running = False

            self.screen.fill((0, 0, 0))
            self.update()
            
        
        #Sortie de boucle -> suppression des sprites, mises a jour de qq variables et vérification des vies du joueur
        for sprite in self._allSprites :
            sprite.kill()
        self.update()
        joueurOK = self._joueur.isAlive()
        if joueurOK and not bigboss : return "continue" #pas de bigboss -> on continue la partie et on passe au niveau suivant
        elif joueurOK and bigboss : return "win"
        elif not joueurOK : return "over"
        
    def update(self) :
        #actualisation de l'affichage graphique
        for sprite in self._allSprites :
            self.screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        clock.tick(25)           #permet de maintenir 25fps

    def terminate(self) :
        pygame.quit()


    #ECRANS
    def Victory(self): #écran victoire
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render('YOU WON!', True, (231, 193, 0))
        textscore = myfont.render('Score:', True, (255, 255, 255))

        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN and self.__class__.lexit.CliqueSourisLabel() : 
                    return 
            self.screen.fill((0, 0, 0))
            self.screen.blit(textsurface,(73,200))
            self.screen.blit(textscore, (100, 600))
            self.screen.blit(self._score, (200, 600))
            self.__class__.lexit.blit(self.screen)
            pygame.display.flip()
            clock.tick(25)

    def GameOver(self): #écran défaite
        myfont = pygame.font.SysFont('Comic Sans MS', 100) #taille + style police du texte
        textsurface = myfont.render('GAME OVER', True, (255, 0, 0)) #texte + lissage + couleur
        textscore = myfont.render('Score:', True, (255, 255, 255))
        scoreNumber = myfont.render(str(self._score), True, (255, 255, 255))

        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN and self.__class__.lexit.CliqueSourisLabel() : 
                    return
            self.screen.fill((0, 0, 0))
            self.screen.blit(textsurface,(50,50)) #affichage texte + position
            self.screen.blit(textscore, (200, 200))
            self.screen.blit(scoreNumber, (225, 300))
            self.__class__.lexit.blit(self.screen)
            pygame.display.flip()
            clock.tick(25)

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
                if event.type == pygame.MOUSEBUTTONDOWN: #faire réagir quand la souris clique
                    if self.__class__.lplay.CliqueSourisLabel() : return True
                    if self.__class__.lexit.CliqueSourisLabel() : return False
       