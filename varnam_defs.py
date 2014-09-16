#!usr/bin/env python
""" Varnam library functions list
"""
# Varnam library functions list
from utils import *
import ctypes as C


class VarnamHandle(C.Structure):
    _fields_ = [('scheme_file', STRING),
                ('suggestions_file', STRING),
                ('internal', VOID)]

VARNAM_PTR = C.POINTER(VarnamHandle)

class Varray(C.Structure):
    _fields_ = [('memory', C.POINTER(VOID)),
                ('allocated', C.c_size_t),
                ('used', C.c_size_t),
                ('index', INT)]


class Token(C.Structure):
    _fields_ = [('id', INT),
                ('type', INT),
                ('match_type', INT),
                ('priority', INT),
                ('accept_condition', INT),
                ('flags', INT),
                ('tag', STRING),
                ('pattern', STRING),
                ('value1', STRING),
                ('value2', STRING),
                ('value3', STRING)]

    
class Word(C.Structure):
    _fields_ = [('text', STRING),
                ('confidence', INT)]

FUNCTION_LIST = [
    ('varnam_init', (STRING, C.POINTER(VARNAM_PTR), C.POINTER(STRING)), INT),
    ('varnam_init_from_lang', (STRING, C.POINTER(VARNAM_PTR), C.POINTER(STRING)), INT),
    ('varnam_version', (), STRING)]
