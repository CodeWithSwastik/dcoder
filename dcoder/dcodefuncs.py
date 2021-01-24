import string

def bin2text(binary_text):
	ascii_string = "".join([chr(int(x, 2)) for x in binary_text.split(" ")])
	return ascii_string 

def text2bin(text):
	bin_string = " ".join(format(ord(x), 'b') for x in text)
	return bin_string 

def oct2text(oct_text):
	ascii_string = ''.join([chr(int(''.join(x), 8)) for x in oct_text.split(" ")])
	return ascii_string 	

def text2oct(text):
	oct_string = " ".join(format(ord(x), "o") for x in text)
	return oct_string 

def hex2text(hex_text):
	ascii_string = ''.join([chr(int(''.join(x), 16)) for x in hex_text.split(" ")])
	return ascii_string 	

def text2hex(text):
	hex_string = " ".join(format(ord(x), "x") for x in text)
	return hex_string 


def text2caesar(text,shift): 
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

def caesar2text(encrypted_text,shift):
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
	posibilities = []

	for shift in range(26):
		decoded = caesar2text(encrypted_text,shift)
		posibilities.append(decoded)

	return posibilities

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

def text2atbash(text):
	return atbash2text(text)

def reverse(text):
	return text[::-1]

def text2railfence(text, key = 3): 

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
	  

def railfence2text(cipher, key = 3): 

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

