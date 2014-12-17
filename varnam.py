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

    def varnam_init(self, scheme_file):
        """
        function to initialize varnam handle
        scheme_file: valid scheme file(*.vst) path
        """
        return self.lib.varnam_init(
            scheme_file, C.byref(self.handle),
            C.byref(self.message))

    def varnam_init_from_lang(self, lang_code):
        """
        Initializes the varnam library from language code
        lang_code: language code in ISO 639-1 format
        """
        return self.lib.varnam_init_from_lang(
            lang_code, C.byref(self.handle),
            C.byref(self.message))

    def varnam_version(self):
        """
        Returns the version of libvarnam
        """
        return self.lib.varnam_version()

    def varnam_transliterate(self, input):
        """
        Performs transliteration on a given input
        Returns: List of transliterations encoded in UTF-8
        input: input word to transliterate
        """
        varray_object = Varray()
        varray_ptr = C.pointer(varray_object)
        res_code = self.lib.varnam_transliterate(self.handle,
                                               input,
                                               C.byref(varray_ptr))
        result = []
        length = self.lib.varray_length(varray_ptr)
        for i in range(length):
            word_ptr = C.cast(self.lib.varray_get(varray_ptr, i),
                              C.POINTER(Word))
            result.append((word_ptr.contents.text,
                           word_ptr.contents.confidence))
        return result
        
