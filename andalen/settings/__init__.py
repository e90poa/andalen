"""
Settings used by andalen project.

This consists of the general production settings, with an optional import of any local
settings.
"""

# Import production settings.
from andalen.settings.production import *

# Import optional local settings.
try:
    from andalen.settings.local import *
except ImportError:
    pass
