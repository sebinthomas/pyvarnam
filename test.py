#!usr/bin/env python
# -*- coding: utf-8 -*-

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

# Test to check if malayalam symbol table is working
TEST_WORD = u"ivan"
TEST_OP = u"ഇവൻ"
TEST_SIZE = 1



class VarnamTrans(unittest.TestCase):
    """ Check the transliteration by setting up some tokens
    """
    def setUp(self):
        self.lib = InternalVarnamLibrary()
        self.handle_object = VarnamHandle()
        self.handle = C.pointer(self.handle_object)
        msg = STRING()
        init_return = self.lib.varnam_init("", C.byref(self.handle), C.byref(msg))
        assert init_return is VARNAM_SUCCESS
        # Creates 3 tokens for testing purposes
        rcode = self.lib.varnam_create_token(self.handle, u"a", u"a-value1", u"a-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        rcode = self.lib.varnam_create_token(self.handle, u"aa", u"aa-value1", u"aa-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        rcode = self.lib.varnam_create_token(self.handle, u"e", u"e-value1", u"e-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        rcode = self.lib.varnam_create_token(self.handle, u"k", u"k-value1", u"k-value2",
                                          u"", u"", VARNAM_TOKEN_CONSONANT, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)

    def test__basic_transliteration(self):
        """ Test to transliterate the tokens we created earlier
        """
        varray_object = Varray()
        varray = C.pointer(varray_object)
        rcode = self.lib.varnam_transliterate(self.handle, u"aek", C.byref(varray))
        self.assertEqual(rcode, VARNAM_SUCCESS)
        self.assertEqual(self.lib.varray_length(varray), 1)
        vword_pointer = C.cast(self.lib.varray_get(varray, 0), C.POINTER(Word))
        vword = vword_pointer.contents
        vword.text = vword.text.decode('utf-8')
        print "value returned by transliterate function: %s"%vword.text
        self.assertEqual(unicode(vword.text), u"a-value1e-value2k-value1")

    def tearDown(self):
        self.lib.varnam_destroy(self.handle)



class VarnamMLTrans(unittest.TestCase):
    """
    Translates a malayalam word ഇവൻ.
    Mainly for seeing if it does transliterate.
    TODO: remove this test.
    """
    def setUp(self):
        self.lib = InternalVarnamLibrary()
        self.handle_object = VarnamHandle()
        self.handle = C.pointer(self.handle_object)
        msg = STRING()
        init = self.lib.varnam_init_from_id('ml', C.byref(self.handle), C.byref(msg))
        assert init is VARNAM_SUCCESS

    def test_transliterate(self):
        """
        deals with transliteration and shows you the O/p
        """
        varray_object = Varray()
        varray = C.pointer(varray_object)
        rcode = self.lib.varnam_transliterate(self.handle, TEST_WORD, C.byref(varray))
        assert rcode is VARNAM_SUCCESS
        size = self.lib.varray_length(varray)
        assert size is TEST_SIZE
        vword_pointer = C.cast(self.lib.varray_get(varray, 0), C.POINTER(Word))
        vword = vword_pointer.contents
        word = vword.text.decode('utf-8')
        print "word is %s and confidence is %d"%(word, vword.confidence)
        self.assertEqual(word, TEST_OP)


if __name__ == '__main__':
    unittest.main()
