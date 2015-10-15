from python_pure import fib
from time import time
from sys import argv

N = int(argv[1])

# Cold run (JIT hasn't seen the code yet)
start = time()
fib(N)
stop = time()
print stop - start,

# Warm up (give the JIT a chance to compile the code).
start = time()
while time() - start < 5:
    fib(N)

start = time()
fib(N)
stop = time()
print stop - start,
