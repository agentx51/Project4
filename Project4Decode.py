"""
Chinmay Pendse
DevPSU Project 4
Pig-Latin
"""
from nltk.corpus import wordnet
def decodePigLatin(text):
	txtList = text.split(" ")

	result = []

	for txt in txtList:
		if(txt[-3:] == 'yay'):
			txt = txt[:-3]
			result.append(txt)
		else:
			txt = txt[:-2]
			temp = txt[-2:] + txt[:-2] 
			if(wordnet.synsets(temp)):
				txt = temp
			else:
				txt = txt[-1] + txt[:-1]
			result.append(txt)

	return " ".join(result)



if __name__ == '__main__':
	x = input("Enter a sentence in Pig Latin: ")
	result = decodePigLatin(x)

	print(result)

