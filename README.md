# dcoder
This is the source code of "dcoder" which a python module that can decode/encode text in various ciphers.

Use "pip install dcoder" and try it out yourself :)

PyPI: https://pypi.org/project/dcoder/

## Usage:

Current commands available are:
    
Encoders:

    text2bin(text)
    text2oct(text)
    text2hex(text)
    text2atbash(text)
    text2caesar(text, shift)
    text2railfence(text, key=3)
Decoders:

    bin2text(binary_text)
    oct2text(oct_text)
    hex2text(hex_text)
    atbash2text(encrypted_text)
    caesar2text(encrypted_text, shift)
    caesarBruteforce(encrypted_text)
    railfence2text(cipher, key=3)
    reverse(text)
