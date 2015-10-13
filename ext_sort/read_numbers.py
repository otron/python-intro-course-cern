#!/bin/python

def make_reader(fname, butts=0):
    # In python 3.x you could use `nonlocal butts` to get around the 
    # UnboundLocalError arising from `butts` being tagged as a local
    # variable of the inner function when we re-bind it at the end.
    # However for now we have to hack around it with a list or something.
    butts = [butts]
    def do_read(step):
        with open(fname, 'r') as f:
            f.seek(butts[0])
            res = [f.readline() for i in range(0, step)]
            butts[0] = f.tell()
        return res

    return do_read

ax = make_reader('nums')
print(ax(3))
print(ax(1))
