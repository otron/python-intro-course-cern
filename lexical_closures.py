def make_adder(n):
    """Returns a new function f(x) --> x+n"""
    def adder(x):
        return n+x
    
    return adder

add3 = make_adder(3)
add9 = make_adder(9)
print add3(4), add9(4)

def make_adder_l(n):
    return lambda x: n+x

ad2 = make_adder_l(2)
print(ad2(5))

make_adder_l2 = lambda x: lambda y: x+y
ad3 = make_adder_l2(3)
print(ad3(2))
