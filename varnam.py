#!usr/bin/env python
"""
The main varnam module.
"""
from library import InternalVarnamLibrary
from utils import *
from varnam_defs import *
from warnings import warn
import ctypes as C

class Varnam:
    """ Varnam class which encapsulates all
         InternalVarnamLibrary calls.
    """
    def __init__(self):
        self.lib = InternalVarnamLibrary()
        self.__handle_obj = VarnamHandle()
        self.handle = C.pointer(self.__handle_obj)
        self.message = STRING()

    def init(self, scheme_file):
        """
        function to initialize varnam handle
        scheme_file: valid scheme file(*.vst) path
        """
        scheme_file_ptr = STRING(scheme_file)
        return self.lib.varnam_init(
            scheme_file_ptr.value, C.byref(self.handle),
            C.byref(self.message))
