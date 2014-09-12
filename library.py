#!usr/bin/env python

# TODO : Comments,docstring, tests,code..

import ctypes as C
from ctypes.util import find_library
import os
import sys
from utils import *

class VarnamLibrary(object):
    """Class which loads the varnam library
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
        self.__status = (0,'')
        # Windowsine avaganikkan paadilello ! 
        if sys.platform == 'win32':
            libFunc = C.windll
        else:
            libFunc = C.cdll

        if not libraryName:
            libraryName = 'varnam'
        getLib = find_library(libraryName)
        if not getLib:
            msg = "Cannot load library name %s .Are you sure varnam was installed correctly ?"%libraryName
            raise VarnamLibraryLoadError(msg)

        try:
            self.lib = getattr(libFunc,getLib)
        except Exception, msg:
            print "Exception occured while loading library: %s"%string(msg)
            self.__status = (1, msg)
                                 
        if self.__status[0] == 0:
            self.__status = (0, "Library loaded at %s"%str(self.lib))

    def status(self):
        return self.__status
