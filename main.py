import party
print('Démarrage...')
party.checkPygameInstallation()

partyRunning = party.Party()

continuer = True
while continuer :
    if partyRunning.playRound() != False :
        party.terminate()
        continuer = False
print("Merci et à bientôt :) !")
        