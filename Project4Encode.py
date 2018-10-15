def toPigLatin(txt):
	txtList = txt.split(" ")
	vowels = ('a', 'e', 'i', 'o', 'u')
	result = []

	for word in txtList:
		if(word.startswith(vowels)):
			result.append(word + 'yay')
		else:
			temp = list(word)
			for x in range(1, len(temp)):
				char = temp[x]
				if(char in vowels):
					result.append(word[x:] + word[0:x] + 'ay')
					break

	return " ".join(result)






if __name__ == '__main__':
	x = input("Enter a sentence to translate to Pig Latin: ")
	result = toPigLatin(x)

	print(result)