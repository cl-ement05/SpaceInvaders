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

class Pygame :
    def __init__(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode([600, 600])
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:             #-> l'utilisateur a demandé à fermer la fenêtre
                    running = False

        pygame.quit()


