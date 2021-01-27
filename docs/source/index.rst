Dcoder 
========================


Overview
--------------------------------------
Welcome to dcoder's Documentation!

docder is a python module that provides various functions for decoding/encoding text. It also has functions for encrypting or decrypting text in various ciphers.

.. warning::

   This module requires Python 3.6 and above due to the use of f-strings in the source code.

It is designed to be simple and easy to use. The functions are very self explanatory but if you need help you can always read the docs here!


Installation
===============================

You can install released versions of dcoder from the Python Package Index with pip or a similar tool:


Stable Release:
------------------
.. code-block:: bash

   pip install dcoder

Working Version: 
-------------------
.. code-block:: bash

   pip install git+https://github.com/CodeWithSwastik/dcoder.git

Basic Usage:
===============================

.. code-block:: python

	>>> import dcoder
	>>> dcoder.text2hex("Hello!") #Encodes the string and returns the hex string
	'48 65 6c 6c 6f 21'
	>>> dcoder.hex2text("48 69 20 74 68 65 72 65 21") #Decodes the hex string and returns the plain text
	'Hi there!'
	>>> dcoder.text2caesar("How are you?") #Encrypts the text in caesar's cipher and returns it
	'Krz duh brx?'
	>>> dcoder.caesar2text("L dp ilqh, wkdqn brx.") #Decrypts the cipher text and returns the decrypted text
	'I am fine, thank you.'


.. toctree::
   :maxdepth: 2
   :caption: Documenation

   ./dcodefuncs

   ./encodefuncs




Miscellaneous
==================

* :ref:`genindex`

* :ref:`modindex`

* :ref:`search`





