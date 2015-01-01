#!usr/bin/env python
""" Internal library class which holds all the bound functions
"""
# TODO : Comments,docstring, tests,code..

import ctypes as C
from ctypes.util import find_library
import os
import sys
from warnings import warn
from utils import *
from varnam_defs import FUNCTION_LIST

class InternalVarnamLibrary(object):
    """Internal class which loads the varnam library
    """
    # Singleton pattern code by Duncan Booth
    __instance = None
    __already_called = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, libraryName=None):
        """ Find the library if not given and initialize
        """
        #nerathe vilichitundenkil inim vilikenda ennu parayan
        if self.__already_called:
            return None
        # Status variable and error code
        self.__status = (0, '')
        # Windowsine avaganikkan paadilello !
        if sys.platform == 'win32':
            libfunc = C.windll
        else:
            libfunc = C.cdll

        if not libraryName:
            libraryName = 'varnam'
        getlib = find_library(libraryName)
        if not getlib:
            msg = ("Cannot load library name %s."
                   "Are you sure varnam was installed correctly ?"%libraryName)
            raise VarnamLibraryLoadError(msg)

        try:
            self.lib = getattr(libfunc, getlib)
        except Exception, msg:
            print "Exception occured while loading library: %s"%str(msg)
            self.__status = (1, msg)
        if self.__status[0] == 0:
            self.__status = (0, "Library loaded at %s"%str(self.lib))
        for function in FUNCTION_LIST:
            try:
                self.bind_function(function)
            except AttributeError, msg:
                warn("Bind error %s "%function[0], VarnamFunctionNotFound)

    def bind_function(self, funcname):
        """ Binds a function to the class from FUNCTION_LIST
        """
        restype = None
        name = funcname[0]
        try:
            args = funcname[1]
        except IndexError:
            args = None
        try:
            restype = funcname[2]
        except IndexError:
            restype = None
        name = name.strip()
        function_name = getattr(self.lib, name)
        setattr(self, name, function_name)
        if args is not None:
            function_name.argtypes = args
        if restype is not None:
            function_name.restype = restype

    def status(self):
        """ Gets you the status of the library
        """
        return self.__status
