class queue:
    """Basic FIFO queue implementation."""
    def __init__(self, initval=None):
        # Rather tedious idiom:
        # If you have a mutable default value, make it None and
        # instead set it inside the function.
        # Default values are defined/bound when the function is created, not when it is run.
        self._q = [] if initval is None else initval
    
    def add(self, *items):
        for i in items:
            self._q.append(i)
    
    def extend(self, iterable):
        self._q.extend(iterable)

    def pop(self):
        try:
            return self._q.pop(0)
        except IndexError:
            raise EmptyQueueError("Cannot pop from empty queue.")

    def __repr__(self):
        return str(self._q)

class counter:
    def __init__(self, start=0):
        self._count = start

    def up(self, n=1):
        self._count += n

    def down(self, n=1):
        self.up(-n)

    def __repr__(self):
        return "counter({0})".format(self._count)
    # This is a poor implementation of __repr__ as it is not readable.

"""Inheritance!"""
class addcounter(counter):
    """Subclass of `counter` which supports the addition operator."""

    def __repr__(self):
        return 'addcounter({.count})'.format(self)
        """__repr__ should return a readable representation of the object.
        readable means we should be able to paste it into our interpreter and get
        an equivalent object back.
        a readable string is valid python code which evaluates to the original expression
        """

    def __add__(self, other):
        return addcounter(self.count + other.count)


eval(str(1/3.)) == 1/3.   # False
eval(repr(1/3.)) == 1/3.  # True

"""Create a slightly enhanced version of the queue class: emergency queue!
It needs to do all the things the queue class can do but also queue-barging.
Queue-barging: stick the thing to the front of the queue."""

class emergencyqueue(queue):
    """Queue implementation with queue-barging capabilities."""
    
    def barge(self, *items):
        """Adds the given items to the front of the queue."""
        # Alternatively:
        # for i, item in enumerate(items):
        #      self.q.insert(i, item)
        for i in reversed(items):
            self.q.insert(0, i)

qu = queue()
eq = emergencyqueue()

"""Python is like Canada. It doesn't enforce class privacy, it just assumes people aren't dicks.
Convention: Names beginning with an underscore refers to objects which
  you should not access directly outside of their defining scope.
Names starting, but not ending, with two underscores are mangled.
Python production code should not rely on class/module names beginning with an underscore.
These aren't a part of the whatever's defined API, which is what you'd expect to not change.
"""
class mangled:
    __a = 3
    def __init__(self):
        self.__b = 5
        self._b = 1

"""In Java, 'private' means private to _this_ class.
'protected' means private to this class and its subclasses."""
bbb = mangled()


"""Polymorphism!

"""

class EmptyQueueError(Exception):
    """Exception thrown when operations which require a non-empty queue
    are performed on an empty queue."""

