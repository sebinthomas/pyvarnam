#!usr/bin/env python

# Utilities for pyvarnam

import ctypes as C

# TODO : all constants for C types over here
# custom exception classes here
# Runtime context picker over here

class VarnamLibraryLoadError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
