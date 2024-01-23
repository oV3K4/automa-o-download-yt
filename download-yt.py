from pytube import YouTube


link = input("Link do vídeo: ")
path = input("Digite o diretório para salvar o vídeo: ")
yt = YouTube(link)

print("Título do vídeo: ", yt.title)
print("Tamanho do vídeo: ", yt.length, "segundos")

ys = yt.streams.get_highest_resolution()

print("Baixando...")
ys.download(path)
print("Download completo!")