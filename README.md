# SpaceInvaders
Jeu SpaceInvaders par Tiphaine Fournier, Paul Cornea et Clément Garrigou

# Prérequis 
- le module pygame doit être installé et disponible ; utilisez la commande ```pip3 install pygame``` si pygame n'est pas installé

# Principes de jeu
- Pas d'infini : Big Boss à la fin donc victoire possible
- Vies du joueur : 3
- 28 ennemis : 4 lignes par 7 colones
- Au début :
  * Ennemi :
    + 40 points de vie
    + 1 missile/12sec
  * Joueur :
    + Lorsque atteint par un missile ennemi : -1 vie
    + 1 missile : 20 dégâts à un ennemi 
- A chaque nouvveau round :
  * Augmentation des points de vie d'un ennemi : + 5

# Options
mettre un nombre X de barrières en fonction du numéro Y du round
