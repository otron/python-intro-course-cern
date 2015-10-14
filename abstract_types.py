"""
Abstract types are defined by the operations that can be performed on it.

FIFO-queue example:
- make a new queue
- add an element to the (back of the) queue
- remove an element from the front of the queue (pop)

"""

"""Classes!

"""

class counter:  # this creates a binding, whoo!
    def __init__(self, start):
        # print dir(self)
        self.count = start
        # print dir(self)

    def up(self, n=1):
        self.count += n
    
    def down(self, n=1):
        self.count -= n

a = counter(10) # a is bound to an instance of 'counter'
a.up(2) # call the `up` method with n=2, increasing a.count from 10 to 12.
a.foo = 9 # a is an object and we can bind whatever to whatever on it.
#print("difference between set of names in scopes of a and counter",
#      list(set(dir(a)) - set(dir(counter))))

"""
special names in python are the ones that are surrounded by double underscores (`__name__`).
colloqially referred to as "magic" names
__init__ abbreviated to dunder-init.
Jacek calls it "magic init".
Magic names are the ones _you_ typically don't access directly but let python
access for you when appropriate.

len(x) --> x.__len__()

When instantiating a class `__new__` gets called somehow?
It returns a fresh, new, untouched instance of whatever class we're instantiating.
__new__ calls __init__ which does the constructing job (i.e. __init__ is the class' constructor).
"__new__ gives birth; __init__ schools it, preparing it for life."
Please do not return anything from init. __new__ does the returning.

"""

# common reasons for name error:
# 1. typo
# 2. looking in the wrong place
# 3. it doesn't exist yet.
# NameErrors are thrown when unqualified name lookups fail
# AttributeErrors are thrown when qualified name lookups fail.
