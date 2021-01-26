from .misc import *
from .textmethods import *
from .decryption import *
from .encryption import *

__title__ = "dcoder"
__summary__ = (
    "dcoder is a module that can decode/encode text in various ciphers."
)
__url__ = "https://github.com/CodeWithSwastik/dcoder"

__version__ = "0.1.2"

__author__ = "Swas.py"
__email__ = "cwswas.py@gmail.com"

__license__ = "MIT License"
__copyright__ = "Copyright 2021 {}".format(__author__)


def get_version():
    return __version__

def get_url(): return __url__

def get_author(): return __author__

def get_license(): return __license__

def get_copyright(): return __copyright__

def get_title(): return __title__

def get_summary():
    return __summary__
