import string

#Encoding

def text2bin(text):
	""" Takes in a string text, returns the encoded text in bin."""

	bin_string = " ".join(format(ord(x), 'b') for x in text)
	return bin_string

def text2oct(text):
	""" Takes in a string text, returns the encoded text in oct."""

	oct_string = " ".join(format(ord(x), "o") for x in text)
	return oct_string 

def text2hex(text):
	""" Takes in a string text, returns the encoded text in hex."""

	hex_string = " ".join(format(ord(x), "x") for x in text)
	return hex_string 

def text2ascii(text):
	""" Takes in a string text, returns the encoded text in ascii."""

	ascii_string = " ".join(format(ord(x))  for x in text)
	return ascii_string


#Encryption

def text2caesar(text,shift = 3): 
	"""
	Returns the encrypted text after encrypting the text with the given shift

		Parameters:
			text (str): The text that needs to be encrypted in Caesar's cipher
			shift (int): The shift that should be used to encrypt the text 

		Returns:
			result (str): The encrypted text
	"""
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
	"""
	Returns the encrypted text after encrypting the text

		Parameters:
			text (str): The text that needs to be encrypted in the Atbash cipher

		Returns:
			translated (str): The encrypted text
	"""
	translated = ""

	for s in text:
		if s.isupper():
			N = ord('Z') + ord('A')
			translated += chr(N - ord(s))
		elif s.islower():
			N = ord('z') + ord('a')
			translated += chr(N - ord(s))
		else:
			translated += s

	return translated

def text2railfence(text, key = 3): 
	"""
	Returns the encrypted text after encrypting the text with the given key

		Parameters:
			text (str): The text that needs to be encrypted in the Railfence cipher
			key (int): The Key that should be used to encrypt the text 

		Returns:
			encrypted (str): The encrypted text
	"""
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
				
	encrypted = "".join(result) 
	return encrypted
	  

