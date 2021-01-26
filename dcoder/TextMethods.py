import string

# TextMethods container class
class TextMethods:
	def __init__(self, text = "No constructor provided"):
		self.text = text
	
	def text2bin(self,text = None):
		if text is None:
			text = self.text
		bin_string = " ".join(format(ord(x), 'b') for x in text)
		return bin_string
		
	def text2oct(self, text = None):
		if text is None:
			text = self.text
		oct_string = " ".join(format(ord(x), "o") for x in text)
		return oct_string 

	def text2hex(self, text = None):
		if text is None:
			text = self.text
		hex_string = " ".join(format(ord(x), "x") for x in text)
		return hex_string 

	def text2ascii(self, text):
		if text is None:
			text = self.text
		ascii_string = " ".join(format(ord(x))  for x in text)
		return ascii_string