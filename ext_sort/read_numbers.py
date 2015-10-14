#!/bin/python

def make_reader(fname, start=0):
    """Returns a function `f(n)` which reads and returns
    the next `n` lines from `fname`.   
    """
    # In python 3.x you could use `nonlocal butts` to get around the 
    # UnboundLocalError arising from `butts` being tagged as a local
    # variable of the inner function when we re-bind it at the end.
    # However for now we have to hack around it with a list or something.
    butts = [start]
    def readnlines(n):
        """Reads the next `n` lines from the closed upon file.
        See also `make_reader`."""
        with open(fname, 'r') as f:
            f.seek(butts[0])
            res = [f.readline() for i in range(n)]
            butts[0] = f.tell()
        return res

    return readnlines

ax = make_reader('nums')

def ext_sort(fname, outf, mem, r_buff, w_buff):
    """Sorts the contents of `fname` using some external sorting algorithm,
    and writes the result to `ouftf.`"""
