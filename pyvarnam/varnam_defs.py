#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Varnam library functions list
"""
# Varnam library functions list
from utils import *
import ctypes as C


#REMINDER: Change this for every major release of varnam

LIBVARNAM_MAJOR_VERSION = 3

VARNAM_PATHS = ['/usr/local/lib', '/usr/local/lib/i386-linux-gnu', '/usr/local/lib/x86_64-linux-gnu', '/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu', '/usr/lib']

VARNAM_NAMES = ['libvarnam.so', "libvarnam.so.{0}".format(LIBVARNAM_MAJOR_VERSION), 'libvarnam.dylib', 'varnam.dll']


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

VARRAY_PTR = C.POINTER(Varray)

class VlearnStatus(C.Structure):
    _fields_ = [('total_words', INT),
                ('failed', INT)]

VLEARN_STATUS_PTR = C.POINTER(VlearnStatus)

#TODO: do we need this ?
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
    ['varnam_init', [STRING, C.POINTER(VARNAM_PTR), C.POINTER(STRING)], INT],
    ['varnam_init_from_id', [STRING, C.POINTER(VARNAM_PTR), C.POINTER(STRING)], INT],
    ['varnam_version', [], STRING],
    ['varnam_transliterate', [VARNAM_PTR, STRING, C.POINTER(VARRAY_PTR)], INT],
    ['varnam_reverse_transliterate', [VARNAM_PTR, STRING, C.POINTER(STRING)], INT],
    ['varnam_detect_lang', [VARNAM_PTR, STRING], INT],
    ['varnam_learn', [VARNAM_PTR, STRING], INT],
    ['varnam_train', [VARNAM_PTR, STRING, STRING], INT],
    ['varnam_learn_from_file', [VARNAM_PTR, STRING, VLEARN_STATUS_PTR, VOID, VOID], INT],
    ['varnam_create_token', [VARNAM_PTR, STRING, STRING, STRING, STRING, STRING, INT, INT, INT, INT, INT], INT],
    ['varnam_set_scheme_details', [VARNAM_PTR, STRING, STRING, STRING, STRING, STRING], INT],
    ['varnam_get_last_error', [VARNAM_PTR], STRING],
    ['varnam_flush_buffer', [VARNAM_PTR], INT],
    ['varnam_config', [], INT],
    ['varnam_get_all_tokens', [VARNAM_PTR, INT, C.POINTER(VARRAY_PTR)], INT],
    ['varray_get', [VARRAY_PTR, INT], VOID],
    ['varray_length', [VARRAY_PTR], INT],
    ['varnam_export_words', [VARNAM_PTR, INT, STRING, INT, VOID], INT],
    ['varnam_import_learnings_from_file', [VARNAM_PTR, STRING, VOID], INT],
    ['varnam_destroy', [VARNAM_PTR], VOID],
    ['varnam_get_scheme_file', [VARNAM_PTR], STRING],
    ['varnam_get_suggestions_file', [VARNAM_PTR], STRING],
    ['varnam_create_token', [VARNAM_PTR, STRING, STRING, STRING, STRING, STRING, INT, INT, INT, INT, INT], INT],
    ['varnam_config']]

# TODO: varnam_learn_from_file uses a callback. So does some other function.
# TODO: varnam_config uses a varargs function.
