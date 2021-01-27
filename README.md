# dcoder 0.2.1

dcoder is a python module that provides various functions for decoding/encoding text. It also has functions for encrypting or decrypting text in various ciphers.


PyPI: https://pypi.org/project/dcoder/ <br>
Docs: https://dcoder.readthedocs.io/en/latest/

## Installation

You can install released versions of dcoder from the Python Package Index with pip or a similar tool:


**Stable Release:** `pip install dcoder`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/dcoder.git`


## Usage:
```python
>>> import dcoder

>>> dcoder.text2hex("Hello!") #Encodes the string and returns the hex string
'48 65 6c 6c 6f 21'
>>> dcoder.hex2text("48 69 20 74 68 65 72 65 21") #Decodes the hex string and returns the plain text
'Hi there!'

>>> dcoder.text2caesar("How are you?") #Encrypts the text in caesar's cipher and returns it
'Krz duh brx?'
>>> dcoder.caesar2text("L dp ilqh, wkdqn brx.") #Decrypts the cipher text and returns the decrypted text
'I am fine, thank you.'
```



## Functions available:

The current list of functions available are:
    
Encoding: 
```python
text2bin(text)
text2oct(text)
text2hex(text)
text2ascii(text)
 ```
Decoding:
 ```python
bin2text(binary_text)
oct2text(oct_text)
hex2text(hex_text)
ascii2text(ascii_text)
```
Encryption:
 ```python
text2atbash(text)
text2caesar(text, shift = 3)
text2railfence(text, key = 3)
```
Decryption:
 ```python
atbash2text(encrypted_text)
caesar2text(encrypted_text, shift = 3)
caesarBruteforce(encrypted_text)
railfence2text(cipher, key = 3)
railfenceBruteforce(encrypted_text)
```

Misc:
```python
reverse(text)
capitalLetterCipher(ciphertext)
firstLetterCipher(ciphertext)
```
    
