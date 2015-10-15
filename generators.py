
def gen_ints(start, stop):
    while start < stop:
        yield start
        start += 1
    return

a = gen_ints(3, 6)
#for i in a: print i

from random import randint
x = gen_ints(0, randint(0, 50))
a = 0

try:
    while True:
        x.next()
        a += 1
except StopIteration:
    pass
#    print("got to {0}".format(a))
finally:
    pass
#    print a

def fib_gen():
    f1, f2 = 1, 0
    while True:
        yield f1
        f1, f2 = f1+f2, f1

a = fib_gen()

def fib_gen_limit(n=float("inf")):
    """iterative fibonacci number generator with optional roof/max n.
    No arg results in an infinite generator."""
    yield 1
    f1, f2 = 1, 0
    while n:
        f1, f2, n = f1+f2, f1, n-1
        yield f1

b = fib_gen_limit(10)

def fibz():
    yield 1; yield 1
    f2 = fibz()
    f1 = fibz(); next(f1) # advance f1 to 1
    # f1 and f2 are now 1 and ??
    while True:
        yield next(f1) + next(f2)
    # third call:
    #   yield 1+1
    #   yield 2+1
    #   yield 3+2
    # won't this get slower and slower and slower and slower?
    # Yuup, it's O(phi**(n)) when called the nth time.
