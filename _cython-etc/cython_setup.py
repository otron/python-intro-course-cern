from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("explicitly_compiled_pure_python", 
                         ["cython_pure.py"]),
               Extension("explicitly_compiled_cython_annotated", 
                         ["cython_with_type_declarations.pyx"])]

setup(
    name = "Cython-test",
    cmdclass = {'build_ext':build_ext},
    ext_modules = ext_modules)

