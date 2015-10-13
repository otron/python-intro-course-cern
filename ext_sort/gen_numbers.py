#!/bin/python
import sys
import random

def do_thing(n, fname='nums', nmin=0, nmax=sys.maxint):
    with open(fname, 'w') as f:
        for i in range(n):
            f.write(str(random.randint(nmin, nmax)) + '\n')

do_thing(10)
