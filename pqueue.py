class priority_queue:

    def __init__(self):
        self.q = [[] for i in range(5)]
    
    def add(self, arg, priority=2):
        if priority < 0:
            raise ValueError("Priority must be in [0, 4].")
        try:
            self.q[priority].append(arg)
        except IndexError:
            raise ValueError("Priority must be in [0, 4].")
        except TypeError:
            raise TypeError("Priority must be an integer.")
        

    def pop(self):
        for li in self.q:
            try:
                return li.pop(0)
            except IndexError:
                continue
        raise EmptyQueue()
    
    def __len__(self):
        return sum(map(len, self.q))


class EmptyQueue(Exception):
    pass

a = priority_queue()
