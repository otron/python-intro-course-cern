"""Descriptors, heyoooo!
A descriptor is an object attribute with binding behavior:
  One whose attribute access has been overriden by methods in the descriptor protocol.
  The methods in the protocol are `__get__()`, `__set__()` and `__delete__()`.
  An object on/for which any of those three methods are defined is said to be a descriptor.

From the pocket reference, pg 129:
  The descriptor methods only apply when an instance of a class defining them (a descriptor class)
  is assigned to a class attribute of another class (known as the _owner_).
  The descriptor methods defined on the descriptor class are then invoked automagically
  upon access to the attribute in the owner class and its instances.

WHEN THEY WRITE `OBJECT ATTRIBUTE` THEY MEAN THAT THE THING IS AN ATTRIBUTE OF THE OWNER WHICH IS AN OBJECT.
NOT EVERYTHING IS AN OBJECT IN PYTHON.
ONLY THE THINGS THAT INHERIT FROM `object` ARE OBJECTS.
SO DESCRIPTOR CLASSES HAVE TO INHERIT FROM `object` OTHERWISE THEY DON'T WORK LOL
This might be related to both classes (owner and descriptor) having to conform to the new style class
thing for it to work in python 2.7.x
Aaand yeah. A new style class in python 2.7.x is one which inherits from `object`.
"""

class desc_fail():
    def __init__(self, val):
        self._val = val
    
    def __get__(self, obj, type=None):
        print("You'll never see this printed.")
        return self._val

class desc_yay(object):
    def __init__(self, val):
        self._val = val

    def __get__(self, obj, objtype):
        print("obj: {0}, objtype: {1}".format(obj, objtype))
        return getattr(obj, self._val)

    def __set__(self, obj, value):
        print("ooh you done setting")
        setattr(obj, self._val, value)
        
class owner(object):
    x = desc_yay('_desc')   # Works!
    dc = desc_yay('_wut')  # Works
#    y = desc_fail(5)  # Doesn't work.
    def __init__(self, val=''):
        self._desc = '?'
        #       self.ix = desc_yay(val)  # Doesn't work.
        #       self.iy = desc_fail(val)  # Doesn't work
        self.dc = val # Works, and is apparently how you're supposed to be using these?
        self.ac = desc_yay(val)
        
a = owner('hello')
# a now has a.x and a.dc which are data descriptors of the desc_yay class
# and are linked to two different private properties of `a` -- a._desc and a._wut,
# which are defined in the class definition.
print('w..')
