"""Memoization -- "it means making memos"."""

def fib_recursive(n):
    if n in [0, 1]:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

fib = fib_recursive
from time import time as gettime
def time(fn, *args, **kwargs):
    start = gettime()
    res = fn(*args, **kwargs)
    return (gettime()-start, res)
    

# lambda implementation
def timel(thunk):
    start = gettime()
    res = thunk()
    return (gettime()-start, res)

# Lambda approach is prettttyyy cool.
print(timel(lambda : fib_recursive(25)))
print(time(fib_recursive, 25))

# "If I find the character sequence 'fib' anywhere in your memoizer I will not be amused"
"""
mfib = memo(fib_recursive)
fib(Q)  --> A in Ts
fib(Q)  --> A in Ts
mfib(Q) --> A in ~Ts
mfib(Q) --> A in ~0s
Check out page 68
"""

# Memoization
# Not a proper solution as the memoization function needs to be general.
def fib_gen():
    resdict = {0: 1, 1: 1}
    def fib(n):
        try:
            return resdict[n]
        except KeyError:
            resdict[n] = fib(n-1) + fib(n-2)
        finally:
            return resdict[n]
    return fib
   
def memo(f):
    resdict = { }
    def func(*args):
        # Initially I tried resdict[*args], not realizing that'd unpack to
        # resdict[n, a, b] which doesn't work (I now know), unlike resdict[(n, a, b)],
        # which does work.
        try:
            return resdict[args]
        except KeyError:
            resdict[args] = f(*args)
            return resdict[args]
    return func

def memo2(f):
    resdict = { }
    # LBYL version of memo()
    def func(*args):
        if not resdict.has_key(args):
            resdict[args] = f(*args)
        return resdict[args]
    
from zlib import crc32
def memo_kwd(f):
    """Memoizer function that handles keyword arguments as well."""
    resdict = { }
    def func(*args, **kwds):
        crc_li = [crc32(a) for a in args]
        for k in kwds:
            crc_li.append(crc32(k, kdws[k]))
        crc_li = sorted(crc_li)
        if not crc_li in resdict:
            resdict[crc_li] = f(*args, **kwds)
        return resdict[crc_li]

def memo_kwd_fset(f):
    """Memoizer function that handles keyword arguments using a frozen set."""
    resdict = { }
    def func(*args, **kwds):
        key = [args, crc32(frozenset(kwds.items()))]
        if not key in resdict:
            resdict[key] = f(*args, **kwds)
        return resdict[key]


def try_finally_fun():
    """Demonstrates how a return statement inside a try block is essentially ignored
    when there's a return statement in the finally block as well."""
    try:
        return 3
    finally:
        print("You see?")
        return 5

def fib_it(n):
    if n in [0, 1]:
        return 1
    fp1, fp2 = 1, 1
    # n-1 b/c we need to do one iteration to get fib(2) right.
    for i in range(n-1):
        fp1, fp2  = fp1 + fp2, fp1
    
    return fp1

def fib_next(f1, f2):
    return (f1+f2, f1)

def fib_itrec(n):
    if n in [0, 1]:
        return 1
    f1, f2 = 1, 1
    for i in range(n-1):
        f1, f2 = fib_next(f1, f2)
    return f1

def fib_itrec(n):
    if n in [0, 1]:
        return 1
    else:
        return fib_itrec2(n, 1, 1)

def fib_itrec2(n, f1, f2):
    # Tail recursion, heyooo.
    if n == 0:
        return f1
    else:
        return fib_itrec2(n-1, f1+f2, f1)

def fib_itrec_single(n, f1=1, f2=0):
    if n < 1:
        return f1
    else:
        return fib_itrec_single(n-1, f1+f2, f1)
