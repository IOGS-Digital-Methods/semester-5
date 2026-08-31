# Proposition d'évaluation BlindTest

Dans ce dossier, on trouvera l'ensemble des codes qui permettent de moduler des sons wav et les démoduler. Le dossier *initial_mp3* contient les musiques que j'ai utilisé pour le blind test. Le code *convert_mp3_to_wav.sh* (code bash) permet de transcrire les 20 premières secondes (options -t 20) de chaque fichier mp3 du dossier en fichier wav dans le dossier *initial_wav*. 

Une fois le dossier *initial_wav* complet, on peut utiliser le notebook [blind_test](blind_test.ipynb) pour créer les sons modulés, qui sont stockés dans le dossier FILES_TO_DECODE. Chaque son du dossier initial_wav est aléatoirement transcris en fichier *am_song_ii.wav* dont la correspondance est donné dans le [fichier texte du même nom](correspondance.txt).
