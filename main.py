import party
print('Démarrage...')
party.checkPygameInstallation()

partyRunning = party.Party()
pygame.display.set_caption("Space Invadors") #changer nom fenêtre

continuer = True
while continuer :
    if partyRunning.playRound() != False :
        party.terminate()
        continuer = False
print("Merci et à bientôt :) !")
        