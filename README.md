# dcoder 0.0.3
This is the source code of "dcoder" which a python module that can decode/encode text in various ciphers. Current Version: 0.0.3

PyPI: https://pypi.org/project/dcoder/

## Installation


**Stable Release:** `pip install dcoder`<br>
**Development Head:** `pip install git+https://github.com/CodeWithSwastik/dcoder.git`


## Usage:

The current list of functions available are:
    
Encoders: 
```python
text2bin(text)
text2oct(text)
text2hex(text)
text2atbash(text)
text2caesar(text, shift)
text2railfence(text, key=3)
 ```
Decoders:
 ```python
bin2text(binary_text)
oct2text(oct_text)
hex2text(hex_text)
atbash2text(encrypted_text)
caesar2text(encrypted_text, shift)
caesarBruteforce(encrypted_text)
railfence2text(cipher, key=3)
reverse(text)
```
    
