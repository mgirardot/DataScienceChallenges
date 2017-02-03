## DataScience Challenge 4
# _ StarCraft _

Starcraft est un jeu vidéo de stratégie en temps réel pratiqué lors de compétitions internationales de sport électronique. Il permet à deux joueurs de s'affronter pour la domination militaire du territoire. Au début du jeu, chaque joueur choisit une des trois races disponibles qui ont différentes capacités et styles de jeu. Les joueurs doivent récolter des ressources pour produire des bâtiments et des unités de combat.

Contrairement à la plupart des jeux de stratégie (échecs, jeu de go, ...), l'ensemble du terrain de jeu n'est pas visible, et chaque joueur doit envoyer des éclaireurs pour identifier le terrain et les positions de son adversaire pour prendre des décisions stratégiques rapidement et efficacement.

[Blizzard](http://eu.blizzard.com/fr-fr/), l'éditeur du jeu, et [DeepMind](https://deepmind.com/), le groupe de recherche en Intelligence Artificielle de Google qui a battu récemment le meilleur joueur de Go, ont annoncé la [création d'une
API](https://deepmind.com/blog/deepmind-and-blizzard-release-starcraft-ii-ai-research-environment/) qui permettra de contrôler de manière programmatique le jeu à partir des informations visuelles. Cet environnement permettra de développer des Intelligences Artificielles capables de résoudre des problèmes plus proche de la complexité des conditions réelles (ex: voiture autonomes).

Pour préparer l'avènement de cette plateforme open source, nous allons, dans ce DataScience Challenge, prédire la victoire des joueurs humains à partir des logs du jeu.

Les données des matches ont été téléchargées sur [ggtracker](http://ggtracker.com/matches), une plateforme d'analyse statistique des replays des joueurs inscrits. Les actions des joueurs ont été extraites à l'aide de l'utilitaire [sc2gears](https://github.com/icza/sc2gears). Les fichiers texte ont été convertis au format csv à l'aide d'un script PowerShell. Les données ont été extraites par un script Python. Le jeu de données `sc2_dataset_5mins.csv` est composé de 240 variables issues de 34579 matches joués.
La cible à prédire est le vainqueur du match indiqué dans la variable `_p1_win_game`.



          \ \
         __\_\
           \__/'/'
          ''  " "

    ________       ___        __  ________
   / ____/ /      ( _ )      / / / / ____/
  / / __/ /      / __ \/|   / /_/ / /_
 / /_/ / /___   / /_/  <   / __  / __/
 \____/_____/   \____/\/  /_/ /_/_/ 


