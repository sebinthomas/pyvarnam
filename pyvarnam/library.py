#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Internal library class which holds all the bound functions
"""
# TODO : Comments,docstring, tests,code..

import ctypes as C
from ctypes.util import find_library
import os
import sys
from warnings import warn
from utils import *
from varnam_defs import *

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

    def __init__(self):
        """ Find the library if not given and initialize
        """
        #nerathe vilichitundenkil inim vilikenda ennu parayan
        if self.__already_called:
            print "Already called me once"
            return None
        # Status variable and error code
        self.__status = (0, '')
        # Windowsine avaganikkan paadilello !
        if sys.platform == 'win32':
            libfunc = C.windll
            self.libcallback = C.WINFUNCTYPE
        else:
            libfunc = C.cdll
            self.libcallback = C.CFUNCTYPE

        # Hardcoding a shared library's path during dev time is
        # preferred by ctypes manual than using ctypes.util.find_library()
        
        getlib = self.find_path()
        if getlib is None:
            msg = "Cannot load library. Are you sure varnam was installed correctly ?"
            raise VarnamLibraryLoadError(msg)
        print "loadpath is {0}".format(getlib)
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

    def find_path(self):
        full_path = None
        for path in VARNAM_PATHS:
            for name in VARNAM_NAMES:
                full_path = os.path.join(path, name)
                if os.path.isfile(full_path):
                    return full_path
        return None


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

    def callback(self, *args):
        return self.libcallback(*args)

    def status(self):
        """ Gets you the status of the library
        """
        return self.__status
