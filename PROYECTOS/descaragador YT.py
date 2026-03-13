import  yt_dlp

url = input("Ingrese el url del video aqui: ")

with yt_dlp.YoutubeDL() as ydl:
    ydl.download([url])

print("El video esta listo.")