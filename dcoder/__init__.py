import string

def bin2text(binary_text):
	ascii_string = "".join([chr(int(x, 2)) for x in binary_text.split(" ")])
	return ascii_string 

def text2bin(text):
	bin_string = " ".join(format(ord(x), 'b') for x in text)
	return bin_string 

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



