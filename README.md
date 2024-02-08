Projet par Jin Alexandre (B2B)

IMPORTANT ! : 

- Si vous avez cette erreur la : "AttributeError: module ‘httpcore’ has no attribute ‘NetworkBackend’” Issue in Python".
  Essayer ces commandes la dans le terminal : - "pip uninstall httpcore"
                                              - "pip install httpcore", ce qui va vous donner un message d'erreur qui vous dit de télécharger une version précise
                                              - "pip install httpcore=(la version demander de télécharger)"

- Si pendant la discussion avec le bot discord ne marche pas, eessayez de répondre une fois de plus (oui ou non ou juste une réponse qui n'a rien a voir avec oui et non), parfois la réponse est émise trop vite ou juste pas pris en compte à certain moment (sûrement à cause d'une complexité d'algorithme trop lourd)

- Si vous avez des erreurs de traduction, ce qui est normal, le module de traduction peut être instable en raison des modfications apportées par Google à son API, de plus nous télécharggons une version non stable

Comment ça marche ? : 

- Pour lancer le bot discord il suffit lancer le programme python (comme d'habitude)

- Changer le token par votre bot discord

- Puis il suffit rentrer les divers commandes afin d'intéragir avec le bot discord !

-----

Prérequis : 

- Installation des paquets : 

- discord : pip install discord

- requests : pip install requests

- googletrans : pip install googletrans==4.0.0-rc1 (obliger de préciser cette version afin d'éviter tout bug)

-----

Fonctionnalités de base: 

- Pour voir votre historique (liée par utilisateur) de commande et mot spécial (commencent par $ ) : !history

- Pour voir la dernière commande rentrée (liée par utilisateur) : !last

- Pour réinialiser l'historique (l'entièreté) : !clear

- Afin de commencer une discussion d'aide sur les commandes : !help 

- Pour réinialiser la discussion d'aide : !reset

- Pour stocker votre historique dans une hasmap (liée par utilisateur) : !store

-----

Fonctionnalités ajoutées : 

- Sauvegarder l'historique contenu dans la hasmap dans un json à l'arrêt du bot (ctrl + c, dans le terminal)

- Afin de traduire vos textes : !translate (langue que vous voulez mettre, cependant vous devez le mettre en anglais) (texte que vous voulez traduire). 
Exemple : "!translate english je suis le bot discord !" ou bien vous n'êtes pas obligé d'écrire la langue en entier : "!translate en je suis le bot discord !"

- Recherche de site ou d'image : !search (type de recherche image ou site) (votre recherche).
Exemple : "!search site python" (pour un site) ou bien "!search image python" (pour une image)

- Météo d'une ville: !weather (ville ou pays en anglais).
Exemple : !weather Paris

-----

Ressources utilisées : 

- Recherche, debug : stackoverflow, github, documentation discord.py & internet en général (pour les petites recherches, de type affichage etc...)

- Pour le json : https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/ 
                 https://www.geeksforgeeks.org/read-json-file-using-python/

- signal (changer le signal du ctrl + c pour ma sauvegarde donnée): https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python 

- googletrans python (traduction): https://www.youtube.com/watch?v=CNohboIuxS4&ab_channel=Francesco 

- résolution de problème googletrans : https://www.reddit.com/r/learnpython/comments/n3w7aw/googletrans_error/
				                       https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
				                       https://github.com/ssut/py-googletrans/issues/366

- weather open api (météo) : https://www.youtube.com/watch?v=9P5MY_2i7K8&ab_channel=NeuralNine

- google search python (Recherche) : https://www.youtube.com/watch?v=CNohboIuxS4&ab_channel=Francesco
