#!usr/bin/env python
""" Varnam constants and function lists
"""
# Varnam constants and function lists
from utils import *
import ctypes as C

class Varnam(C.Structure):
    __fields__ = [('scheme_file', STRING),
                  ('suggestions_file', STRING),
                  ('internal', VOID)]

VARNAM_PTR = C.POINTER(Varnam)

FUNCTION_LIST = [
    ('varnam_init', (STRING, C.POINTER(VARNAM_PTR), C.POINTER(STRING)), INT)]
