def sortnames_first(fname='/etc/passwd'):
    """Reads the passwd file and sorts its contents by the third column."""
    with open(fname, 'r') as f:
        contents = f.read()

    # Trim away the newline at the end of the contents (gotcha lol)
    # Split on newline ('\n')
    c2 = contents.strip().split('\n')

    # c2 contains a list of strings, we to split each string on ':'
    c3 = [x.split(':') for x in c2]

    # Now we can sort it.
    # Second gotcha: they're strings. We want to sort 'em like they're numbers.
    # Gotta convert the key to an int.
    c4 = sorted(c3, key=lambda x: int(x[2]))
    
    return c4

def sortnames_perexample(fname='/etc/passwd'):
    """Reads the passwd file (or whichever file is specified by `fname`) and sorts it by the third column.
    More closely resembles the example(s) given by the instructor than sortnames_first()"""
    with open(fname, 'r') as f:
        res = []
        for line in f:
            # '_' is used in python to indicate a variable we don't care about.
            uname, _, uid, _ = line.split(':', 3)
            res.append((uname, int(uid)))
        res.sort(key=lambda x: x[1])
                
    return res

import itertools
def printcmp(f1=sortnames_first, f2=sortnames_perexample):
    """Calls the two given function and prints their results in a print-friendly-ish manner.
    Assumes f1 returns a list with x[0] == uname, x[2] == uid
    and f2 a sequence with x[0] == uname, x[1] == uid"""
    for ax, bx in itertools.izip(enumerate(f1()), enumerate(f2())):
        # [ab]x[0] == iterator #
        # ax[1] == list, uname = ax[1][0], uid = ax[1][2]
        # bx[1] == [uname, uid]
        print ax[0], "->", ax[1][0], ax[1][2], " -- ", bx[1][0], bx[1][1]
        
# printcmp()

def my_keygen(n):
    def _getkey(seq):
        return seq[n]
    
    return _getkey

def my_cmpgen(n):
    def _cmp(a, b):
        return cmp(a[n], b[n])
    return _cmp

a = my_cmpgen(0)
print(a([0], [1]))

# The process of rewriting a multi-argument function to a
# single-argument function that returns another single-argument function
# that returns a... that returns the same result as the multi-argument function
# is called currying.
# For a function f(x, a) -> z we would have a function g(x) -> h, h(a) -> z

# Do the thing again but with functools.partial with the non-curried version of key()
