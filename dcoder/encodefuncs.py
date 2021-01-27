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
	  

