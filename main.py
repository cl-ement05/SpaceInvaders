print('Démarrage...')
import party
party.checkPygameInstallation()

partyRunning = party.Party()
if partyRunning.Welcome() :
    continuer = True
    while continuer :
        if partyRunning.playRound() == False :
            partyRunning.terminate()
            continuer = False

print("Merci et à bientôt :) !")

