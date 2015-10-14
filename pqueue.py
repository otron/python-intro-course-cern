from collections import deque

class priority_queue:

    def __init__(self):
#        self.q = [[] for i in range(5)]
        # using deque instead of list halves the time lol
        self._q = [ deque() for i in range(5)]
    
    def add(self, arg, priority=2):
        if priority < 0:
            raise ValueError("Priority must be in [0, 4].")
        try:
            self._q[priority].append(arg)
        except IndexError:
            raise ValueError("Priority must be in [0, 4].")
        except TypeError:
            raise TypeError("Priority must be an integer.")
        

    # This one's faster
    def pop(self):
        for li in self._q:
            if li:
                return li.popleft()
        raise EmptyQueue()

    # This one's prettier
    def pop_old(self):
        for li in self._q:
            try:
                return li.popleft()
            except IndexError:
                continue
        else:
            raise EmptyQueue()
    
    def __len__(self):
        return sum(map(len, self._q))


class EmptyQueue(Exception):
    pass

a = priority_queue()
