# SpaceInvaders
Jeu SpaceInvaders par Tiphaine Fournier, Paul Cornea et Clément Garrigou

# Prérequis 
- le module pygame doit être installé et disponible ; utilisez la commande ```pip3 install pygame``` si pygame n'est pas installé

# Principes de jeu
- 1 round de party.py = 1 round du jeu
- Pas d'infini : Big Boss à la fin donc victoire possible
- 35 ennemis : 5 lignes par 7 colones
- On définit la carte de jeu comme un carré de 7 cases par 7, chacune de 100 pixels de côté
- Les ennemis occupent un rectangle de 5 cases de haut par 7 de large soit 35 ennemis ; il reste alors 2 lignes de cases dont 1 pour le joueur
- Au début :
  * Ennemi :
    + 40 points de vie
    + 1 missile/12sec
  * Joueur et ses pioupious :
    + Lorsque atteint par un missile ennemi : -1 vie
    + 1 missile : 20 dégâts à un ennemi 
    + 3 vies
- A chaque nouvveau round :
  * Augmentation des points de vie d'un ennemi : + 5

# Options
mettre un nombre X de barrières en fonction du numéro Y du round

# Arborescence du projet
Le schéma qui va suivre représente chaque fichier du projet et les dépendances qu'il peut avoir. Il est donc essentiel qu'il soit respecté lors du développement
```
|
|-main.py -> programme principal, maître
  |- party.py -> classe contenant des infos contenant la partie (score...), gère tous les objets comme les ennemis, missiles...; s'occupe de l'affichage -> mise à jour faite grâce à l'appel de fonction (playRound()), création d'ennemis... ; 1 instance devrait être créée dans le main
    |- pygame.py -> permet de stocker des vars du pygame (écran, la surface) mais c'est une data class : elle ne sert qu'à stocker des données, on n'exécute aucune fonction ; 1 instance devrait être crée par party.py
    |- ennemi.py -> autant d'instances que nécessaire, créées par party.py
    |- joueur.py -> représente le personnage, ses vies... ; 1 seule instance devrait être créée par party.py et conservée tout au long d'une même partie 
    |- pioupiou.py
```

# répartition
-Paul : Les pioupiou et le joueur
-Clément : les méchants 
-Tiphaine : le score, la map (faire des étoiles), écrans de start et de game over