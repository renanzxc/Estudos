import os
from tinytag import TinyTag

#Detecta músicas com bitrate menor que 320kbps de acordo com a minha distribuição de pastas.
directory = "/mnt/c/Users/Renan Gustavo/Music/"
# python3 detectMusics > musicLow.txt

def main(directory):
	artists = os.listdir(directory) #Recupera as pastas com o nomes dos artistas e coloca em uma lista
	results = []
	for artist in artists:
		if not "." in artist:
			albums = os.listdir(directory+artist)
			for possibleMusic in albums:
				if ".mp3" in possibleMusic:
					musicLow = TinyTag.get(directory+artist+"/"+possibleMusic)
					if(musicLow.bitrate<320.0):
						result = {"Artist": artist, "Music": possibleMusic}
						results.append(result)

				else:
					album = possibleMusic
					if not "." in album:
						musics = os.listdir(directory+artist+"/"+album)
						for music in musics:
							if ".mp3" in music:
								musicLow = TinyTag.get(directory+artist+"/"+album+"/"+music)
								if(musicLow.bitrate<320.0):
									result = {"Artist": artist,"Album": album, "Music": music}
									results.append(result)
	print(results)

if __name__ == "__main__":
	main(directory)

								
