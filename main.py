from party import Party
print('Démarrage...')

party = Party()

continuer = True
while continuer :
    status = party.playRound()
    if status != None :
        party.terminate()
        continuer = False
        