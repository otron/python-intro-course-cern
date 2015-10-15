
class Rectangle(object):
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def geta(self):
        return self.w * self.h

    def seta(self, val):
        self.w = float(val) / self.h
    
    a = property(geta, seta)
        

r = Rectangle(2, 3)
assert r.w == 2
assert r.h == 3
assert r.a == 2*3

r.w = 4
assert r.w == 4
assert r.h == 3
assert r.a == 4*3


r.a = 24
assert r.a == 24
assert r.w == 8
assert r.h == 3
        
print "OK"
