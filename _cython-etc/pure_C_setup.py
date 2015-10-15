
from distutils.core import setup, Extension

setup(name="ctypes-test",
      ext_modules = [Extension("C", ["C.c"])])
