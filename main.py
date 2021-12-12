print('Démarrage...')
import party

partyRunning = party.Party()
if partyRunning.Welcome() :
    continuer = True
    while continuer :
        status = partyRunning.playRound()
        if status == "quit" :
            partyRunning.terminate()
            continuer = False
        elif status == "over" :
            partyRunning.GameOver()
            partyRunning.terminate()
            continuer = False
        elif status == "win" :
            partyRunning.Victory()
            partyRunning.terminate()
            continuer = False

print("Merci et à bientôt :) !")

