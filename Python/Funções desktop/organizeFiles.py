import os
import shutil

#Verifica se existe uma imagem com esse nome na pasta, se não ele a move.
directorySrc = "/mnt/c/Users/Renan Gustavo/Desktop/new/musicas/"
directoryDst = "/mnt/c/Users/Renan Gustavo/Desktop/new/musicas2/"


foldersSrc = os.listdir(directorySrc)


for folderSrc in foldersSrc: #Percorre as pasta na pasta de origem
	filesSrc = os.listdir(directorySrc+folderSrc)
	filesDst = os.listdir(directoryDst+folderSrc)
	for fileSrc in filesSrc: #Percorre os arquivos da pasta que está dentro da pasta origem
		if not fileSrc in filesDst:
			shutil.copy(directorySrc+folderSrc+"/"+fileSrc,directoryDst+folderSrc+"/"+fileSrc) #Copia o arquivo do primeiro diretetório para o segundo
		else:
			pass
	
	for fileDst in filesDst: #Percorre os arquivos da pasta de destino
		if "." in fileDst:	#Verifica se todos os arquivos tem '.' no nome, isso para evitar mover pastas para a outra pasta
			if not fileDst in filesSrc: # Verifica se o arquivo não está na pasta de origem
				try:
					shutil.move(directoryDst+folderSrc+"/"+fileDst,directoryDst+folderSrc+"/trash/"+fileDst) #Se não estiver ele move o arquivo do diretório de destivo é movido para a pasta trash
				except:
					os.mkdir(directoryDst+folderSrc+"/trash/")#Se não existir a pasta trash no diretório ela será criada
					shutil.move(directoryDst+folderSrc+"/"+fileDst,directoryDst+folderSrc+"/trash/"+fileDst)	
			else:
				pass

