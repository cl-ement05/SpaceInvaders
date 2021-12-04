import party
print('Démarrage...')
party.checkPygameInstallation()

partyRunning = party.Party()

continuer = True
while continuer :
    status = partyRunning.playRound()
    if status != None :
        party.terminate()
        continuer = False
        