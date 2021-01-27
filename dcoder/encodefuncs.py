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
