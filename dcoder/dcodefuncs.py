import string


#Encoding

def text2bin(text):
	bin_string = " ".join(format(ord(x), 'b') for x in text)
	return bin_string

def text2oct(text):
	oct_string = " ".join(format(ord(x), "o") for x in text)
	return oct_string 

def text2hex(text):
	hex_string = " ".join(format(ord(x), "x") for x in text)
	return hex_string 

def text2ascii(text):
	ascii_string = " ".join(format(ord(x))  for x in text)
	return ascii_string


#Decoding

noSpaceError = "No spaces were found in the {}. The output might be not be correct if the input text is not correctly formatted."


def bin2text(binary_text):

	#Raise exception if there are no spaces in the text
	if not " " in binary_text and len(binary_text)>8:
		raise ValueError(noSpaceError.format("binary_text"))

	binary_text = binary_text.strip()

	#Converts the bin to text
	plain_string = "".join([chr(int(x, 2)) for x in binary_text.split(" ")])
	return plain_string 


def oct2text(oct_text):

	#Raise exception if there are no spaces in the text
	if not " " in oct_text and len(oct_text)>3:
		raise ValueError(noSpaceError.format("oct_text"))

	oct2text = oct2text.strip()

	#Converts the oct to text
	plain_string = ''.join([chr(int(''.join(x), 8)) for x in oct_text.split(" ")])
	return plain_string 	

def hex2text(hex_text):

	#Raise exception if there are no spaces in the text
	if not " " in hex_text and len(hex_text)>2:
		raise ValueError(noSpaceError.format("hex_text"))

	hex_text = hex_text.strip()

	#Converts the hex to text
	plain_string = ''.join([chr(int(''.join(x), 16)) for x in hex_text.split(" ")])
	return plain_string 	

def ascii2text(ascii_text):

	#Raise exception if there are no spaces in the text
	if not " " in ascii_text and len(ascii_text)>3:
		raise ValueError(noSpaceError.format("ascii_text"))

	ascii2text = ascii2text.strip()

	#Converts the ascii to plain text
	plain_string = ''.join([chr(int(''.join(x))) for x in ascii_text.split(" ")])
	return plain_string



#Encryption

def text2caesar(text,shift = 3): 
	result = "" 
 
	for i in range(len(text)): 
		char = text[i] 
  
		if char.isupper(): 
			result += chr((ord(char) + shift-65) % 26 + 65) 
		elif char.islower(): 
			result += chr((ord(char) + shift - 97) % 26 + 97) 
		else:
			result += char
	return result 

def text2atbash(text):
	return atbash2text(text)

def text2railfence(text, key = 3): 

	text = text.replace("\n", "")

	rail = [['\n' for i in range(len(text))] 
				  for j in range(key)] 
	  
	dir_down = False
	row, col = 0, 0
	  
	for i in range(len(text)): 
		  
 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		  

		rail[row][col] = text[i] 
		col += 1
		   
		if dir_down: 
			row += 1
		else: 
			row -= 1

	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return "" . join(result) 
	  



#Decryption

def caesar2text(encrypted_text,shift = 3):
	translated = ""

	for symbol in encrypted_text:
		if symbol == " ":
			translated += " "			
		elif symbol.isupper():
			num = string.ascii_uppercase.find(symbol) - shift
			if num < 0:
				num += 26
			translated += string.ascii_uppercase[num]
		elif symbol.islower():
			num = string.ascii_lowercase.find(symbol) - shift
			if num < 0:
				num += 26
			translated += string.ascii_lowercase[num]
		else:
			translated += symbol

	return translated

def caesarBruteforce(encrypted_text):  
	possibilities = []

	for shift in range(26):
		decoded = caesar2text(encrypted_text,shift)
		possibilities.append(decoded)

	return possibilities

def atbash2text(encrypted_text):
	translated = ""

	for s in encrypted_text:
		if s.isupper():
			N = ord('Z') + ord('A')
			translated += chr(N - ord(s))
		elif s.islower():
			N = ord('z') + ord('a')
			translated += chr(N - ord(s))
		else:
			translated += s

	return translated

def railfence2text(cipher, key = 3): 

	cipher = cipher.replace("\n", "")

	rail = [['\n' for i in range(len(cipher))]  
				  for j in range(key)] 
	  

	dir_down = None
	row, col = 0, 0
	  

	for i in range(len(cipher)): 
		if row == 0: 
			dir_down = True
		if row == key - 1: 
			dir_down = False
		  
		rail[row][col] = '*'
		col += 1
		  

		if dir_down: 
			row += 1
		else: 
			row -= 1
	index = 0
	for i in range(key): 
		for j in range(len(cipher)): 
			if ((rail[i][j] == '*') and
			   (index < len(cipher))): 
				rail[i][j] = cipher[index] 
				index += 1
		  

	result = [] 
	row, col = 0, 0
	for i in range(len(cipher)): 
		  
 
		if row == 0: 
			dir_down = True
		if row == key-1: 
			dir_down = False
			  
 
		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
			  

		if dir_down: 
			row += 1
		else: 
			row -= 1
	return "".join(result)



#Misc 

def reverse(text):
	''' Reverses the text in the argument '''
	return text[::-1]

def capitalLettersCipher(ciphertext):
	""" 

	Returns the capital letters in the ciphertext

	Example:

	Cipher Text: dogs are cuter than HorsEs in a LooP. 
	Decoded Text: HELP """  

	return "".join([i for i in ciphertext if i.isupper()])


def firstLetterCipher(ciphertext):
	""" 
	Returns the first letters of each word in the ciphertext

	Example:

	Cipher Text: Horses evertime look positive
	Decoded text: Help """  

	ciphertext = ciphertext.strip()

	return "".join([i[0] for i in ciphertext.split(" ")])
