# SpaceInvaders
Jeu SpaceInvaders par Tiphaine Fournier, Paul Cornea et Clément Garrigou

# Prérequis 
- le module pygame doit être installé et disponible ; utilisez la commande ```pip3 install pygame``` si pygame n'est pas installé

# Principes de jeu
- 1 round de party.py = 1 round du jeu
- Pas d'infini : Big Boss à la fin donc victoire possible
- Fenetre de 700 pixels par 700
- On définit la carte de jeu comme un carré de 6 cases par 6, chacune de 100 pixels de côté et une marge de 50 pixel pour chaque côté du carré
- Les ennemis occupent un rectangle de 4 cases de haut par 6 de long soit 24 ennemis ; il reste alors 2 lignes de cases dont 1 pour le joueur
- Les ennemis commençent "à gauche" de la map. Le centre d'un ennemi a donc pour coordonnées min (100, 100) (son coin gauche est à (50, 50)) et max (600, 400)
- Le centre du joueur lui se balade sur une droite d'équation y = 600
- Au début :
  * Ennemi :
    + 40 points de vie
    + 1 missile/12sec
  * Joueur et ses pioupious :
    + Lorsque atteint par un missile ennemi : -1 vie
    + 1 missile : 40 dégâts à un ennemi 
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