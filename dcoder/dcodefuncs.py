import string

#Decoding
noSpaceError = "No spaces were found in the {}. The output might be not be correct if the input text is not correctly formatted."

def bin2text(binary_text):
	""" Takes in a string binary_text, returns the decoded plain text."""

	#Raise exception if there are no spaces in the text
	if not " " in binary_text and len(binary_text)>8:
		raise ValueError(noSpaceError.format("binary_text"))

	binary_text = binary_text.strip()

	#Converts the bin to text
	plain_string = "".join([chr(int(x, 2)) for x in binary_text.split(" ")])
	return plain_string 

def oct2text(oct_text):
	""" Takes in a string oct_text, returns the decoded plain text."""


	#Raise exception if there are no spaces in the text
	if not " " in oct_text and len(oct_text)>3:
		raise ValueError(noSpaceError.format("oct_text"))

	oct_text = oct_text.strip()

	#Converts the oct to text
	plain_string = ''.join([chr(int(''.join(x), 8)) for x in oct_text.split(" ")])
	return plain_string 	

def hex2text(hex_text):
	""" Takes in a string hex_text, returns the decoded plain text."""

	#Raise exception if there are no spaces in the text
	if not " " in hex_text and len(hex_text)>2:
		raise ValueError(noSpaceError.format("hex_text"))

	hex_text = hex_text.strip()

	#Converts the hex to text
	plain_string = ''.join([chr(int(''.join(x), 16)) for x in hex_text.split(" ")])
	return plain_string 	

def ascii2text(ascii_text):
	""" Takes in a string ascii_text, returns the decoded plain text."""

	#Raise exception if there are no spaces in the text
	if not " " in ascii_text and len(ascii_text)>3:
		raise ValueError(noSpaceError.format("ascii_text"))

	ascii_text = ascii_text.strip()

	#Converts the ascii to plain text
	plain_string = ''.join([chr(int(''.join(x))) for x in ascii_text.split(" ")])
	return plain_string


#Decryption
def caesar2text(encrypted_text,shift = 3):
	"""
	Returns the decrypted text after decrypting the encrypted_text

		Parameters:
			encrypted_text (str): The encrypted text in Caesar's cipher
			shift (int): The shift that should be used to decrypt the text 

		Returns:
			translated (str): The decrypted text
	"""
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
	"""
	Returns a list of all the possibilities after decrypting the encrypted_text without using a shift.

		Parameters:
			encrypted_text (str): The encrypted text in Caesar's cipher

		Returns:
			possibilities (list): All the possibilities of decryption
	"""
	possibilities = []

	for shift in range(26):
		decoded = caesar2text(encrypted_text,shift)
		possibilities.append(decoded)

	return possibilities

def atbash2text(encrypted_text):
	"""
	Returns the decrypted text after decrypting the encrypted_text

		Parameters:
			encrypted_text (str): The encrypted text in Atbash cipher

		Returns:
			translated (str): The decrypted text
	"""

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
	"""
	Returns the decrypted text after decrypting the encrypted_text.

		Parameters:
			encrypted_text (str): The encrypted text in railfence cipher
			key (int): The Key or the height of the rails 

		Returns:
			translated (str): The decrypted text
	"""

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

def railfenceBruteforce(encrypted_text):  
	"""
	Returns a list of all the possibilities after decrypting the encrypted_text without using a shift.

		Parameters:
			encrypted_text (str): The encrypted text in Railfence Cipher

		Returns:
			possibilities (list): All the possibilities of decryption
	"""
	possibilities = []

	n = len(encrypted_text)

	for key in range(2,n):
		decoded = railfence2text(encrypted_text,key)
		possibilities.append(decoded)

	return possibilities

#Misc 
def reverse(text):
	''' Takes in a string text, returns the text reversed'''
	return text[::-1]

def capitalLettersCipher(ciphertext):
	""" 

	Returns the capital letters in the ciphertext

		Parameters:
			ciphertext (str): The encrypted text

		Returns:
			plaintext (str): The decrypted text

		Example:

			Cipher Text: dogs are cuter than HorsEs in a LooP. 

			Decoded Text: HELP """  


	plaintext = "".join([i for i in ciphertext if i.isupper()])
	return plaintext

def firstLetterCipher(ciphertext):
	""" 
	Returns the first letters of each word in the ciphertext

		Parameters:
			ciphertext (str): The encrypted text

		Returns:
			plaintext (str): The decrypted text

		Example:

			Cipher Text: Horses evertime look positive

			Decoded text: Help
	"""  

	ciphertext = ciphertext.strip()

	plaintext = "".join([i[0] for i in ciphertext.split(" ")])
	return plaintext
