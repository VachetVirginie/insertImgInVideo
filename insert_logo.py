import subprocess

def insert_logo(input_video, logo_path, output_video):
    # Redimensionner le logo à la taille souhaitée
    cmd_resize = [
        'ffmpeg', '-i', logo_path, '-vf', 'scale=120:-1', 'resized_logo.png'
    ]
    subprocess.run(cmd_resize, check=True)

    # Commande FFmpeg pour insérer le logo en bas à gauche
    cmd_insert = [
        'ffmpeg', '-i', input_video, '-i', 'resized_logo.png',
        '-filter_complex', '[0:v][1:v]overlay=10:H-h-10', output_video
    ]

    try:
        subprocess.run(cmd_insert, check=True)
        print("Logo inséré avec succès.")
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'insertion du logo :", e)

# Chemin vers la vidéo d'entrée, le logo et la vidéo de sortie
input_video_path = './videoInput/video_entree.mp4'
logo_path = './logo/logo.png'
output_video_path = './videoOutput/video_sortie.mp4'

# Appel de la fonction pour insérer le logo
insert_logo(input_video_path, logo_path, output_video_path)
