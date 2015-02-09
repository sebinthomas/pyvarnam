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
        self.__vlearn_status_obj = VlearnStatus()
        self.learn_status = C.pointer(self.__vlearn_status_obj)
        self.learn_callback = self.lib.callback(VOID, VARNAM_PTR, STRING,
                                                INT, VOID)

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
        
        Returns: tuple of transliterations encoded in UTF-8
                 and their confidence values.
        input: input word to transliterate.
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

    def varnam_create_token(self, pattern, value1, value2, value3,
                            tag, token_type, match_type, priority,
                            accept_condition, buffered):
        """creates a token

        for more info regarding parameters look into api.h
        """
        res_code = self.lib.varnam_create_token(self.handle,
                                                pattern, value1,
                                                value2, value3,
                                                tag, token_type,
                                                match_type, priority,
                                                accept_condition,
                                                buffered)
        return res_code

    def varnam_learn(self, word):
        """
        Varnam will learn the supplied word and possible
        ways to write it.
        
        word: const char* string to learn
        """
        res_code = self.lib.varnam_learn(self.handle, word)
        return res_code

    def varnam_train(self, pattern, word):
        """
        Trains varnam to associate a pattern with the word
        pattern: const char* string pattern
        
        word: const char* string word
        """
        res_code = self.lib.varnam_train(self.handle, pattern, word)
        return res_code

    def varnam_config(self, type, *args):
        """
        Varnam configuration.

        Does not persist. Resets to default when varnam_init()
        is called again
        """
        res_code = self.lib.varnam_config(self.handle, type, *args)
        return res_code

    def varnam_learn_from_file(self, filepath, callback):
        """
        Varnam learns from the file specified.

        filepath: File to learn
        callback: callback function invoked on each word
                  consult api.h for more information
        """
        l_callback = self.learn_callback(callback)
        res_code = self.lib.varnam_learn_from_file(self.handle, filepath,
                                                   self.learn_status, l_callback,
                                                   None)

    
    
