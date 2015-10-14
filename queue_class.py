class queue:
    """Basic FIFO queue implementation."""
    def __init__(self, initval=None):
        # Rather tedious idiom:
        # If you have a mutable default value, make it None and
        # instead set it inside the function.
        # Default values are defined/bound when the function is created, not when it is run.
        self.q = [] if initval is None else initval
    
    def add(self, *items):
        for i in items:
            self.q.append(i)
    
    def extend(self, iterable):
        self.q.extend(iterable)

    def pop(self):
        return self.q.pop(0)

    def __repr__(self):
        return str(self.q)

class counter:
    def __init__(self, start=0):
        self.count = start

    def up(self, n=1):
        self.count += n

    def down(self, n=1):
        self.up(-n)

    def __repr__(self):
        return "counter at {0}".format(self.count)
