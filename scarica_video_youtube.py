import os
import yt_dlp

# Inserisci qui il link dello Shorts o del video di YouTube
url_youtube = "https://www.youtube.com/shorts/jOkXxxCrR8Y"

# Percorso in cui salvare il file sul tuo PC
video_output = r"c:\test\youtube\video.mp4"

# Crea la cartella di destinazione se non esiste
os.makedirs(os.path.dirname(video_output), exist_ok=True)

# Configurazione yt-dlp: scarica SOLO il video, ignorando l'audio
#    'format': 'bestvideo[height<=480][ext=mp4]/bestvideo[height<=480]',
#    'format': 'bestvideo[ext=mp4]/bestvideo', # Prende solo il video migliore in MP4 

ydl_opts = {
    'format': 'bestvideo[height<=720][ext=mp4]/bestvideo[height<=720]',
    'outtmpl': video_output,
    'overwrites': True,
    'quiet': False  # Mostra l'avanzamento del download nel prompt DOS
}

print("Inizio download della sola traccia video da YouTube (Niente Audio = Nessun obbligo di FFmpeg)...")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_youtube])
    print(f"\nDownload completato con successo! File salvato in:\n{video_output}")
except Exception as e:
    print(f"\nErrore durante il download: {e}")


