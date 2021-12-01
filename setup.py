from distutils.core import setup, Extension
setup(name='search', version='1.0',  \
      ext_modules=[Extension('search', ['python.cpp'])])

# setup(name='spam', version='1.0',  \
#       ext_modules=[Extension('spam', ['hello.cpp'])])