"""
Compares the performance of some simple code (recursive Fibonacci)
implemented in:

+ Pure Python
+ Pure Python compiled with Cython
+ Type-annotated Cython compiled with Cython
+ Pure C accessed from Python with Ctypes
"""

import timeit
import sys

try:
    input_value = int(sys.argv[1])
except (IndexError, ValueError):
    raise SystemExit("You must specify an integer (the input to fib) as the first command line argument.")

from contextlib import contextmanager
@contextmanager
def report_progress(message):
    """Context manager. Prints MESSAGE, executes block. Prints 'done'
    when finished."""
    print "-----", message
    sys.stdout.flush()
    try:
        yield
    finally:
        print "----- done"
        print
        sys.stdout.flush()


print
print '========== Compliling and loading =============='
print 

with report_progress('Importing pure python module'):
    import python_pure

import subprocess
with report_progress("Explicitly Cython-compiling"):
    subprocess.check_call("python cython_setup.py install --install-lib=.", shell=True)
    import explicitly_compiled_pure_python
    import explicitly_compiled_cython_annotated

with report_progress("Compiling pure C implementation"):
    subprocess.check_call("python pure_C_setup.py install --install-lib=.", shell=True)

with report_progress("Using ctypes to load C implementation"):
    import ctypes
    if sys.platform == 'darwin':
        libfib = ctypes.CDLL('C.so', ctypes.RTLD_GLOBAL)
    else:
        import os
        libfib = ctypes.CDLL("%s/%s" % (os.getcwd(),'C.so'), ctypes.RTLD_GLOBAL)
    fib = libfib.fib

with report_progress('Installing pyximport: will automatically use Cython to compile on import'):
    import pyximport
    pyximport.install(pyimport = True)
    # From now on, Cython will attempt to compile anything that is
    # imported.

with report_progress('Pyximporting pure python compiled with Cython'):
    # Pyximport will magically compile this on import
    import cython_pure

with report_progress('Pyximporting Cython with type declarations'):
    # Pyximport will magically compile this on import
    import cython_with_type_declarations

with report_progress('Looking for pypy'):
    pypy_found = not subprocess.call('which pypy', shell=True)
    if pypy_found:
        print 'pypy found'
    else:
        print 'pypy not found'


################## data gathering ###############
data = {}

def time(module, input_value):
    """Times how long the fib implmentation provided by MODULE takes
    to run when given INPUT_VALUE. Tries to adapt the number of
    invocations of fib so that the total run time is around 1
    second. Returns the average time taken per invocaton."""
    t = timeit.Timer("fib(%d)" % (input_value,),
                     "from %s import fib" % (module.__name__,))
    total_time = t.timeit(1)
    repetitions = 1
    # If the execution time is very short, keep increasing it until it
    # is at least 0.2s. Report the average time taken.
    while total_time < 0.2:
        repetitions *= 10
        total_time = t.timeit(repetitions)
    return total_time / repetitions

def run_time(msg, module, input_value):
    """Prints MSG. Times the fib implementation provided by
    MODULE. Stores the result in the global dictionary DATA."""
    print "Timing %s: " % (msg,),
    sys.stdout.flush()
    data[msg] = time(module, input_value)
    print data[msg]

# Dummy function to help access this module
def x(): pass
this_module = sys.modules[x.__module__]

print
print '=============== Live timings ==================='
print 
run_time("Pure python                               ", python_pure, input_value)
run_time("Pure python through Cython (pyximport)    ", cython_pure, input_value)
run_time("Cython with type declarations (pyximport) ", cython_with_type_declarations, input_value)
run_time("Pure C via ctypes                         ", this_module, input_value)
run_time("Pure python through Cython (distutils)    ", explicitly_compiled_pure_python, input_value)
run_time("Cython with type declarations (distutils) ", explicitly_compiled_cython_annotated, input_value)

if pypy_found:
    print 'Timing pypy     (approximate)                    : ',
    sys.stdout.flush()
    import os, shlex
    command = shlex.split('pypy time_pypy.py %d' % input_value)
    pypy_results = subprocess.check_output(command, cwd=os.getcwd())
    print pypy_results.strip()
    pypy_cold, pypy_warm = map(float, pypy_results.split())
    data['PyPy cold                                '] = pypy_cold
    data['PyPy warm                                '] = pypy_warm

print
print '============= Relative timings ================='
print 

base = min(data.values())
for k in data:
    data[k] /= base

sorted_data = sorted(data.items(), key=lambda (msg,time): time)

# Print table of relative run times stored in DATA. For each result,
# print one column, with that result expressed as the base time (1.0)
# and the other results scaled relative to it.
for (msg, base_time) in sorted_data:
    for (_, other_time) in sorted_data:
        relative_time = base_time / other_time
        # if relative_time < 1:
        #     relative_time = -1.0 / relative_time
        print "%9.3f" % (relative_time,),
    print "  ", msg
print
