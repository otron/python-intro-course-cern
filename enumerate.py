def genumerate(arg, i=0):
    for x in arg:
        yield i, x
        i += 1

import itertools
def ienumerate(arg, i=0):
    return itertools.izip(itertools.count(i), arg)

af = ienumerate(range(3))


class cenumerate_fail:
    # Bzzzst. Haha oh wow.
    def __init__(self, data, start=0):
        self._i = start
        self._data = data
        self._c = 0
    
    def __iter__(self):
        return self
    
    def next(self):
        try:
            return self._i+self._c, next(self._data)
        except TypeError:
            try:
                return self._i+self._c, self._data[self._c]
            except IndexError:
                raise StopIteration
        finally:
            self._c += 1

class cenumerate:
    def __init__(self, data, start=0):
        # The trick is to use the built in iter() function
        # WELL THAT MAKES IT EASIER
        self._iter = iter(data)
        self._i = start

    def next(self):
        self._i += 1
        return self._i-1, next(self._iter)

    def __iter__(self):
        return self
        
        

xs = cenumerate('hello', 3)
ys = enumerate('hello', 3)
