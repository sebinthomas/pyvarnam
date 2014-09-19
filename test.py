#!usr/bin/env python

# really quick and dirty test to get across the point
# that nothing is really working

""" Transliteration Test """

from library import InternalVarnamLibrary
from varnam_defs import *
from utils import *
from constants import *
import ctypes as C
import unittest
import os

FILE_NAME = "testfile"

# there is probably no need for this
# but it is late and I can't think
def get_a_file(name):
    file_handle = open(name, 'a')
    return file_handle

class VarnamTrans(unittest.TestCase):
    """ Check the transliteration by setting up some tokens
    """
    def setUp(self):
        self.lib = InternalVarnamLibrary()
        self.handle = VARNAM_PTR()
        msg = STRING()
        self.scheme_file = get_a_file(FILE_NAME)
        init_return = self.lib.varnam_init(FILE_NAME, C.byref(self.handle), C.byref(msg))
        assert init_return is VARNAM_SUCCESS

    def test_create_token(self):
        """ This test creates three tokens
        """
        rcode = self.lib.varnam_create_token(self.handle, "a", "a-value1", "a-value2",
                                          "", "", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        rcode = self.lib.varnam_create_token(self.handle, "e", "e-value1", "e-value2",
                                          "", "", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        rcode = self.lib.varnam_create_token(self.handle, "k", "k-value1", "k-value2",
                                          "", "", VARNAM_TOKEN_CONSONANT, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)

    def test_transliterate(self):
        """ Test to transliterate the tokens we created earlier
        """
        words = VARRAY_PTR()
        rcode = self.lib.varnam_transliterate(self.handle, "aek", C.byref(words))
        self.assertEqual(rcode, VARNAM_SUCCESS)
        self.assertEqual(self.lib.varray_length(words), 1)
        single_word = Word(self.lib.varray_get(words, 0))
        print single_word.text
        self.assertEqual(single_word.text, "a-value1e-value2k-value1")

    def tearDown(self):
        self.lib.varnam_destroy(self.handle)
        self.scheme_file.close()
        os.remove(FILE_NAME)

if __name__ == '__main__':
    unittest.main()
