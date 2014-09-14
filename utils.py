#!usr/bin/env python
"""Utilities for pyvarnam
"""
# Utilities for pyvarnam

import ctypes as C

# TODO : all constants for C types over here
# custom exception classes here
# Runtime context picker over here

VOID = C.c_void_p
INT = C.c_int
BOOL = C.c_bool
STRING = C.c_char_p

# custom exceptions
class VarnamLibraryLoadError(Exception):
    """ When library cannot be loaded
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#custom warnings
class VarnamFunctionNotFound(UserWarning):
    """ When the specified function hasn't been found
        in the library
    """
