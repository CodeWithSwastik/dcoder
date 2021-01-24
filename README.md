# dcoder 0.1.0
This is the source code of "dcoder" which a python module that provides various functions for decoding/encoding text. It also has functions for encrypting or decrypting text in various ciphers.

PyPI: https://pypi.org/project/dcoder/


## Installation

You can install released versions of dcoder from the Python Package Index with pip or a similar tool:


**Stable Release:** `pip install dcoder`<br>
**Working Version:** `pip install git+https://github.com/CodeWithSwastik/dcoder.git`


## Usage:

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
```

Misc:
```python
reverse(text)
```
    
