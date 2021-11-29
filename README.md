# SpaceInvaders
Jeu SpaceInvaders par Tiphaine Fournier, Paul Cornea et Clément Garrigou

# Prérequis 
- le module pygame doit être installé et disponible ; utilisez la commande ```pip3 install pygame``` si pygame n'est pas installé

# Principes de jeu
- 1 round de party.py = 1 round du jeu
- Pas d'infini : Big Boss à la fin donc victoire possible
- 28 ennemis : 4 lignes par 7 colones
- On définit la carte de jeu comme un carré de 60 cases par 60, chacune de 10 pixels de côté
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
  |- party.py -> classe contenant des infos contenant la partie (score...), gère tous les objets comme les ennemis, missiles...; 1 instance devrait être créée dans le main
    |- pygame.py -> s'occupe de l'affichage -> mise à jour faite grâce à l'appel de fonctions (par ex lorsqu'un nouvel ennemi est créé par party.py, c'est party qui va appeler une fonction Pygame.nouveaumissile() pour signaler le nouvel élément et que pygame adapte l'affichage en csq) ; 1 instance devrait être crée par party.py
    |- ennemi.py -> autant d'instances que nécessaire, créées par party.py
    |- joueur.py -> représente le personnage, ses vies... ; 1 seule instance devrait être créée par party.py et conservée tout au long d'une même partie 
    |- pioupiou.py
```

# répartition
-Paul : Les pioupiou et le joueur
-Clément : les méchants 
-Tiphaine : le score et la map 