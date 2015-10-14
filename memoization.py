"""Memoization -- "it means making memos"."""

def fib_recursive(n):
    if n in [0, 1]:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

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
