def uno(_):
    return 1

def inc(n):
    return n+1

def inc_by(n):
    def inc(m):
        return n+m
    return inc

class INC_BY:
    def __init__(self, n):
        self.n = n

    def __call__(self,n):
        return n + self.n

@INC_BY(100)
@inc_by(10) # ... inc_by(10) = inc ? wat
@inc # ... `uno = inc`
@uno # funny way of writing `hello = uno`
def hello():
    print 'hi'

#print hello # 1 gets printed

# wait, what?
def inc_result_by(n):
    def decorator(fn):
        def proxy(*args, **kwds):
            return fn(*args, **kwds) + n
        return proxy
    return decorator

def WRAPS(original):
    def decorator(proxy):
        proxy.__name__ = original.__name__
        proxy.__doc__ = original.__doc__
        proxy.__module__ = original.__module__
        return proxy
    return decorator

def report_args(fn):
    @WRAPS(fn)
    def proxy(*args, **kwds):
        print args, kwds
        return fn(*args, **kwds)
    return proxy

def report_result(fn):
    @wraps(fn)
    def proxy(*args, **kwds):
        res = fn(*args, **kwds)
        print res
        return res
    return proxy

from functools import wraps
@inc_result_by(10)
@report_result
@report_args
def snafu_add(a,b):
    "borked up addition"
    return a*b

print snafu_add(2, 3)
