import os 
from mutagen.easyid3 import EasyID3

directory = "/mnt/c/Users/Renan Gustavo/Desktop/new/musicas/"

# Function to rename multiple files 
def main(directory): 

	for oldName in os.listdir(directory): 
		musicTags = EasyID3(directory+oldName)
		newName = musicTags['title'][0]+".mp3"
		src = directory + oldName
		dst = directory + newName
		  
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 

# Driver Code 
if __name__ == '__main__': 

	# Calling main() function 
	main(directory) 