# Pyvarnam

```
     _     _
    /  \  /  \         |
    \_//  \_//  /\_____|
     _     |_   _ _ _ 
    ( )_| (|_) ()| | )O
    ===================
     
```
Pyvarnam is a python wrapper to the [libvarnam](https://github.com/varnamproject/libvarnam) library.

[Varnam](http://www.varnamproject.com/) is an open-source transliterator suited for Indian languages and the
main component is a C library called `libvarnam`. Pyvarnam provides python bindings for libvarnam.

##### Installation

You need to install libvarnam for pyvarnam to work. You could refer [libvarnam installation](https://github.com/varnamproject/libvarnam#installing-libvarnam) to find out how to install libvarnam.

Download the archive, un-tar/zip and 'cd' into the directory you unzipped the
archive into and then run

```

 user@user-pc:~/dir-where-you-unzipped$ python setup.py install
```
 

##### Usage

To transliterate with pyvarnam, you just have to run the following.
```
from pyvarnam import varnam

var_lib=varnam()
var_lib.varnam_init_from_id("ml")
result = var_lib.varnam_transliterate("varnam")
if result is not None:
    print result[0][0]
    
```
As of now only some of the functions mentioned in libvarnam/api.h has been implemented. You could refer `varnam.py` to
see which all functions are available. 

##### Running the tests

A basic test suite has been implemented based on the transliteration tests in
libvarnam. To run them, run

```
python test.py
```
Currently pyvarnam has only been tested in linux. If you find any bugs or feel the need to refactor the code,
don't hesitate to submit a pull request :)