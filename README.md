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
- Les ennemis commençent "à gauche" de la map. Le centre d'un ennemi a donc pour coordonnées min (50, 100) (son coin gauche est à (0, 50)) et max (650, 400)
- Le centre du joueur lui se balade sur une droite d'équation y = 600
- Au début :
  * Ennemi :
    + 1 vie
    + 1 missile/4sec
  * Boss :
    + Attend le joueur bien sagement au 10e round
    + 10 vies
  * Joueur et ses pioupious :
    + Lorsque atteint par un missile ennemi : -1 vie
    + 1 missile : retire 1 vie aux ennemis (les petits meurent)
    + 3 vies
- A chaque nouveau round :
  * Augmentation de la vitesse de tir des pioupious ennemis

# Options
On a de la musique

# Arborescence du projet
Le schéma qui va suivre représente chaque fichier du projet et les dépendances qu'il peut avoir. Il est donc essentiel qu'il soit respecté lors du développement
```
|
|-main.py -> programme principal, maître
  |- party.py -> classe contenant des infos contenant la partie (score...), gère tous les objets comme les ennemis, missiles...; s'occupe de l'affichage -> mise à jour ; 1 instance devrait être créée dans le main
    |- ennemi.py -> autant d'instances que nécessaire, créées par party.py ; contient également la classe bigboss qui hérite de ennemi
    |- joueur.py -> représente le personnage, ses vies... ; 1 seule instance devrait être créée par party.py et conservée tout au long d'une même partie 
    |- pioupiou.py -> autant d'instances que nécessaire, créées par party.py ; contient la classe Pioupiou mère (ne jamais utiliser cette classe !) et les 2 classes filles pour différencier les pioupious joueur et ennemi
    |- pygamelabel.py -> classe utilisée pour afficher les labels cliquables/interactifs
```

# répartition
-Paul : Les pioupiou, le joueur, les images, le ReadMe et pré-alpha du jeu(=les tests).
-Clément : les méchants, le fonctionnement général une fois tout réunit, ajustements suite à la pré-alpha.
-Tiphaine : le score, la map, écrans de start et de game over et la présentation
