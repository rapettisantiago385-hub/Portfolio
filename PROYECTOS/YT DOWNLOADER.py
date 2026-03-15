import yt_dlp

url = input("Ingrese el url del video aqui: ")

opciones = {
    'format': 'best',
    'outtmpl': '/storage/emulated/0/Download/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(opciones) as ydl:
    ydl.download([url])

print("El video esta listo.")