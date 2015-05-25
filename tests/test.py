#!usr/bin/env python
# -*- coding: utf-8 -*-

# really quick and dirty test to get across the point
# that nothing is really working

""" Transliteration Test """


from pyvarnam import Varnam
from pyvarnam.constants import *
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
        self.lib = Varnam()
        init_return = self.lib.varnam_init()
        assert init_return is VARNAM_SUCCESS
        print "Initialized varnam library by calling varnam_init()"
        rcode = self.lib.varnam_create_token(u"a", u"a-value1", u"a-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        print "SUCCESS: Token 'a' with value 'a-value1' and 'a-value2' created"
        rcode = self.lib.varnam_create_token(u"aa", u"aa-value1", u"aa-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        print "SUCCESS: Token 'aa' with  value 'aa-value1' and 'aa-value2' created"
        rcode = self.lib.varnam_create_token(u"e", u"e-value1", u"e-value2",
                                          u"", u"", VARNAM_TOKEN_VOWEL, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        print "SUCCESS: Token 'e' with value 'e-value1' and 'e-value2' created"
        rcode = self.lib.varnam_create_token(u"k", u"k-value1", u"k-value2",
                                          u"", u"", VARNAM_TOKEN_CONSONANT, VARNAM_MATCH_EXACT, 0, 0, 0)
        self.assertEqual(rcode, VARNAM_SUCCESS)
        print "SUCCESS: Token 'k' with value 'k-value1' and 'k-value2' created"

    def test__basic_transliteration(self):
        """ Test to transliterate the tokens we created earlier
        """
        try:
            result = self.lib.varnam_transliterate(u"aek")
            word = result[0][0]
            self.assertEqual(result[0][0], u"a-value1e-value2k-value1")
            print "SUCCESS: transliterating 'aek' gives 'a-value1e-value2k-value1'"
        except VarnamResultNotSuccess:
            self.fail("varnam_transliterate did not return VARNAM_SUCCESS")

    def tearDown(self):
        self.lib.varnam_destroy()

class VarnamMLTransliterationTest(unittest.TestCase):
    """
    Test that Transliterates "ivan" 
    to a malayalam word ഇവൻ.
    """
    def setUp(self):
        """
        Tries to initialize the varnam library 
        for malayalam language
        """
        self.lib = Varnam()
        rcode = self.lib.varnam_init_from_id("ml")
        assert rcode is VARNAM_SUCCESS
        print "SUCCESS: Initialized varnam library with symbol file for malayalam"

    def test_transliterate(self):
        """
        Tries to transliterate the word 'ivan'
        """
        try:
            result = self.lib.varnam_transliterate(TEST_WORD)
            word = result[0][0]
            self.assertEqual(word,TEST_OP)
            print "SUCCESS: transliterated output for %s is %s"% (TEST_WORD, word)
        except VarnamResultNotSuccess:
            self.fail("varnam_transliterate did not return VARNAM_SUCCESS")

    def tearDown(self):
        self.lib.varnam_destroy()
        
if __name__ == '__main__':
    unittest.main()
