try : 
    import pygame
except ImportError :
    print("Erreur : le module pygame est requis pour le bon fonctionnement de ce jeu")
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

from random import choice
from joueur import Joueur
from ennemi import BigBoss, Ennemi

#init de pygame et chargement en mémoire des sons, du background...
pygame.init()
background = pygame.image.load("images/background.jpg")

#audio
pygame.mixer.init()
firePioupiou = pygame.mixer.Sound("audio/shoot.wav")
ennemiKilled = pygame.mixer.Sound("audio/invaderkilled.wav")
mainMusic = pygame.mixer.music.load("audio/spaceinvaders1.wav")
playerDeath = pygame.mixer.Sound("audio/explosion.wav")
pygame.mixer.music.set_volume(0.5)

clock = pygame.time.Clock()
pygame.display.set_caption("Space Invadors")
from pygamelabel import Label                     #on importe ici car pour initialiser des fonts, pygame.init() doit avoir tourné

class Party :    
    lexit = Label("Exit", 350, 600) #création bouton exit
    lplay = Label("Play", 350, 500) #création bouton play
    
    def __init__(self) -> None:
        self._screen = pygame.display.set_mode([700, 700])
        self._level = 0
        self._joueur = Joueur()
        self._allSprites = pygame.sprite.Group()
        self._listEnnemiPioupiou = pygame.sprite.Group()
        self._joueurPioupiou = pygame.sprite.Group()
        self.ENNEMIPIOUPIOU = pygame.USEREVENT + 1
        self.ENNEMIDIRECTION = pygame.USEREVENT + 2
        self._score = 0
        pygame.mixer.music.play(loops=-1)

        #récupération s'il existe d'un high score
        try :
            with open("data", "r") as file :
                fileData = file.readline()
            highscore = fileData.split("=")[1]
            self._highscore = int(highscore)
        except (FileNotFoundError, IOError, ValueError) :
            self._highscore = 0
            with open("data", "w") as file :
                file.write("highscore=0")
        
    def playRound(self) :
        self._allSprites.add(self._joueur)
        self._listEnnemis = pygame.sprite.Group()

        #init et création des ennemis
        #si on atteint le niveau 10, big boss
        if self._level == 9 :
            boss = BigBoss((250, 250))
            self._listEnnemis.add(boss)
            self._allSprites.add(boss)
            bigboss = True
        else :
            bigboss = False
            for y in range(4) :
                for x in range(6) :
                    newEnnemy = Ennemi((50 + 100 * x, 100 + y * 100), "blue_space_invader.jpg" if y < 2 else "space_invader.jpg")        #on met des invaders bleus sur les 2 premières lignes
                    self._listEnnemis.add(newEnnemy)
                    self._allSprites.add(newEnnemy)
        self.update()

        #Déclaration des events custom
        pygame.time.set_timer(self.ENNEMIPIOUPIOU, 4000 - 400 * self._level)
        pygame.time.set_timer(self.ENNEMIDIRECTION, 1000)                       #permet de faire le va et vient des ennemis ; toutes les secondes : changement de direction

        ennemiMoveDirection = 0                        #compteur utilisé pour faire bouger 5 fois les ennemis vers la droite de 4 pixels, puis la même chose vers la gauche et ainsi de suite

        #labels pour pouvoir afficher le score, les points de vie du joueur et le niveau de la partie durant le jeu
        igfont = pygame.font.SysFont('Comic Sans MS', 26) #taille + style police du texte
        Levellabel = igfont.render('Level:', True, (53, 196, 38))
        Scorelabel = igfont.render('Score:', True, (248, 233, 0))
        Lifelabel = igfont.render('Life:', True, (241, 57, 57))
        
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
                if len(self._joueurPioupiou.sprites()) == 0 :                   #on vérifie que aucun missile n'est "en cours"    
                    newPioupiou = self._joueur.instantiatePioupiou()
                    self._allSprites.add(newPioupiou)
                    self._joueurPioupiou.add(newPioupiou)
                    firePioupiou.play()

            #MISE A JOUR DES POSITIONS
            self._listEnnemis.update("right" if ennemiMoveDirection % 2 == 0 else "left")       #nombre pair -> les ennemis vont vers la droite sinon ils vont à gauche
            for pioupiou in self._listEnnemiPioupiou :
                pioupiou.update()
            for pioupiou in self._joueurPioupiou.sprites() :
                pioupiou.update()

            #GESTION DES COLLISIONS
            collideJoueurPioupiouE = pygame.sprite.spritecollideany(self._joueur, self._listEnnemiPioupiou)   #=sprite d'un pioupiou ennemi s'il touche le joueur
            if collideJoueurPioupiouE :
                self._joueur.diminuerVie(1)
                collideJoueurPioupiouE.kill()
                running = False
                playerDeath.play()
            
            ennemiCollideDict = pygame.sprite.groupcollide(self._listEnnemis, self._joueurPioupiou, False, False)   #on récupère l'ennemi qui a été touché par le missile du joueur
            if ennemiCollideDict :
                for ennemi in ennemiCollideDict.keys() :
                    if not bigboss :               #si pas en mode bigboss -> le missile du joueur tue l'ennemi instantanément
                        ennemi.kill()
                        ennemiCollideDict[ennemi][0].kill()
                    else : 
                        ennemi.retirerVie(1)                               #sinon on retire une vie au bigboss (il faut 10 missiles pour le tuer)
                        ennemiCollideDict[ennemi][0].kill()
                        if not ennemi.isAlive() : ennemi.kill() 
                    self._score += 10
                    ennemiKilled.play()
                if len(self._listEnnemis.sprites()) == 0 :     
                    self._level += 1
                    running = False
            
            self._screen.blit(background, (0, 0))
            ScoreNumberig = igfont.render(str(self._score), True, (255, 255, 255))
            LifeNumber = igfont.render(str(self._joueur._vie), True, (255, 255, 255))
            LevelNumber = igfont.render(str(self._level + 1), True, (255, 255, 255))
            self._screen.blit(Lifelabel, (20, 17))
            self._screen.blit(LifeNumber, (80, 17))
            self._screen.blit(Scorelabel, (270, 17))
            self._screen.blit(ScoreNumberig, (355, 17))
            self._screen.blit(Levellabel, (580, 17))
            self._screen.blit(LevelNumber, (654, 17))
            self.update()
            
        
        #Sortie de boucle -> suppression des sprites, mises a jour de qq variables et vérification des vies du joueur
        for sprite in self._allSprites :
            sprite.kill()
        self.update()
        joueurOK = self._joueur.isAlive()
        if not bigboss : 
            if joueurOK : return "continue" #pas de bigboss -> on continue la partie et on passe au niveau suivant
            else : return "over"
        else :
            if joueurOK and boss.isAlive() : return "continue"
            if joueurOK and not boss.isAlive() : return "win"
            else : return "over"
        
    def update(self) :
        #actualisation de l'affichage graphique
        for sprite in self._allSprites :
            self._screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        clock.tick(25)           #permet de maintenir 25fps

    def terminate(self) :
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()


    #ECRANS
    def Victory(self): #écran victoire
        self.endScreen('YOU WON', (231, 193, 0))

    def GameOver(self): #écran défaite
        self.endScreen("GAME OVER", (255, 0, 0))

    def endScreen(self, text: str, textcolor: tuple) :
        if self._highscore != None : 
            if self._score > self._highscore :
                with open("data", "w") as file :
                    file.write("highscore=" + str(self._score))
                highscore = Label("New highscore ! " + str(self._score), 350, 500)
            else :
                highscore = Label("Highscore : " + str(self._highscore), 350, 500)
        
        myfont = pygame.font.SysFont('Comic Sans MS', 100) #taille + style police du texte
        textsurface = myfont.render(text, True, textcolor) #texte + lissage + couleur
        textscore = myfont.render('Score:', True, (255, 255, 255))
        scoreNumber = myfont.render(str(self._score), True, (255, 255, 255))

        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN and self.__class__.lexit.CliqueSourisLabel() : 
                    return
            self._screen.blit(background, (0, 0))
            self._screen.blit(textsurface,(50,50)) #affichage texte + position
            self._screen.blit(textscore, (200, 200))
            self._screen.blit(scoreNumber, (225, 300))
            self.__class__.lexit.blit(self._screen)
            if self._highscore != None : highscore.blit(self._screen)
            pygame.display.flip()
            clock.tick(25)

    def Welcome(self): #Ecran de démarrage
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        myfont2 = pygame.font.SysFont('Comic Sans MS', 75) #police + taille
        textWelcome = myfont.render('Welcome to', True, (255, 255, 255)) 
        textgame = myfont2.render('SPACE INVADERS', True, (255, 255, 255)) #texte + antialiasing + couleur
        self._screen.blit(background, (0, 0))
        self._screen.blit(textWelcome,(220,260)) 
        self._screen.blit(textgame, (10,300)) #texte à afficher + position
        self.__class__.lexit.blit(self._screen)
        self.__class__.lplay.blit(self._screen)
        pygame.display.flip()
        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN: #faire réagir quand la souris clique
                    if self.__class__.lplay.CliqueSourisLabel() : return True
                    if self.__class__.lexit.CliqueSourisLabel() : return False
       