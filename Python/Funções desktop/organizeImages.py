import os
import shutil

#Verifica se existe uma imagem com esse nome na pasta, se não ele a move.
directorySrc = "/mnt/c/Users/Renan Gustavo/Desktop/new/imagens/"
directoryDst = "/mnt/c/Users/Renan Gustavo/Google Drive/Fotos/"

imagesSrc = os.listdir(directorySrc)
imagesDst = os.listdir(directoryDst)

for imageSrc in imagesSrc:
	if not imageSrc in imagesDst:
		shutil.move(directorySrc+imageSrc,directoryDst+imageSrc) #Se a imagem do diretório raiz não estiver no diretório destino a imagem será movida
	else:
		pass