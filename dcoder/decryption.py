import string
class Decryption:
    def caesar2text(self, encrypted_text,shift = 3):
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

    def caesarBruteforce(self,encrypted_text):  
        posibilities = []

        for shift in range(26):
            decoded = caesar2text(encrypted_text,shift)
            posibilities.append(decoded)

        return posibilities

    def atbash2text(self, encrypted_text):
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

    def railfence2text(self, cipher, key = 3): 

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