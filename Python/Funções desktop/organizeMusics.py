import os
import shutil
from mutagen.easyid3 import EasyID3

directory = "/mnt/c/Users/Renan Gustavo/Desktop/new/musicas/"
#Verifica no artista e o album da música criando o diretório "artista/album/musica.mp3"

def main(directory):
	musics = os.listdir(directory)
	for music in musics:
		musicTags = EasyID3(directory+music)
		artist = musicTags['artist'][0]
		album = musicTags['album'][0]
		if not os.path.exists(directory+artist):
			os.makedirs(directory+artist)
			os.makedirs(directory+artist+"/"+album)
		elif not os.path.exists(directory+artist+"/"+album):
			os.makedirs(directory+artist+"/"+album)

		shutil.move(directory+music,directory+artist+"/"+album)

if __name__ == "__main__":
	main(directory)
	