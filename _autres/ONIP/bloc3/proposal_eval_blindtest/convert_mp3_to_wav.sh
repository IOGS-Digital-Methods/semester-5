#!/bin/bash

# Spécifier le chemin du dossier contenant les fichiers MP3
dossier_mp3="initial_mp3"

# Spécifier le chemin du dossier de sortie pour les fichiers WAV
dossier_wav="initial_wav"

# Assurez-vous que le dossier de sortie existe, sinon créez-le
mkdir -p "$dossier_wav"

# Parcourir tous les fichiers dans le dossier MP3
for fichier_mp3 in "$dossier_mp3"/*.mp3; do
    nom_sans_extension=$(basename "$fichier_mp3" .mp3)
    fichier_wav="$dossier_wav/${nom_sans_extension}.wav"

    # Utiliser ffmpeg pour tronquer et convertir le fichier MP3 en WAV
    # on ne garde que les 20 premières secondes
    ffmpeg -i "$fichier_mp3" -t 20 -ac 2 -ar 44100 "$fichier_wav"

    echo "Troncature et conversion de $fichier_mp3 terminées avec succès."
done

echo "Troncature et conversion terminées avec succès pour tous les fichiers MP3."

