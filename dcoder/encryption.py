import string
# Encryption
class Encyption:
    def text2caesar(self, text,shift = 3): 
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

    def text2atbash(self, text):
        return atbash2text(text)

    def text2railfence(self, text, key = 3): 

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