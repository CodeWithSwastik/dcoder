import string

class Misc:
    def reverse(self,text):
        ''' Reverses the text in the arguement '''
        return text[::-1]

    def capitalLettersCipher(self, ciphertext):
        """ 

        Returns the capital letters in the ciphertext

        Example:

        Cipher Text: dogs are cuter than HorsEs in a LooP. 
        Decoded Text: HELP """  

        return "".join([i for i in ciphertext if i.isupper()])


    def firstLetterCipher(self, ciphertext):
        """ 
        Returns the first letters of each word in the ciphertext

        Example:

        Cipher Text: Horses evertime look positive
        Decoded text: Help """  

        return "".join([i[0] for i in ciphertext.split(" ")])

    self.noSpaceError = "No spaces were found in the {}. The output might be not be correct if the input text is not correctly formatted."

    def bin2text(self, binary_text):
        # Raise exception if there are no spaces in the text
        if not " " in binary_text and len(binary_text)>8:
            raise ValueError(self.noSpaceError.format("binary_text"))

        # Converts the bin to text
        plain_string = "".join([chr(int(x, 2)) for x in binary_text.split(" ")])
        return plain_string


    def oct2text(self,oct_text):
        # Raise exception if there are no spaces in the text
        if not " " in oct_text and len(oct_text)>3:
            raise ValueError(self.noSpaceError.format("oct_text"))

        # Converts the oct to text
        plain_string = ''.join([chr(int(''.join(x), 8)) for x in oct_text.split(" ")])
        return plain_string 	

    def hex2text(self, hex_text):

        # Raise exception if there are no spaces in the text
        if not " " in hex_text and len(hex_text)>2:
            raise ValueError(self.noSpaceError.format("hex_text"))

        # Converts the hex to text
        plain_string = ''.join([chr(int(''.join(x), 16)) for x in hex_text.split(" ")])
        return plain_string 	

    def ascii2text(self, ascii_text):

        #Raise exception if there are no spaces in the text
        if not " " in ascii_text and len(ascii_text)>3:
            raise ValueError(self.noSpaceError.format("ascii_text"))

        #Converts the ascii to plain text
        plain_string = ''.join([chr(int(''.join(x))) for x in ascii_text.split(" ")])
        return plain_string