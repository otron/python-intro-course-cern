def one(*args):
    return args

def wone(args):
    return args

# wone(1, 2)  # TypeError
print(one(1, 'butts', 44))  # (1, 'butts', 44)
print('www')

def two(a=1, b='w'):
    """Keyword parameters are parameters given default values.
    """
    return a, b

def three(*args, **kwds):
    """`*args` collects "all remaining positional arguments".
    `**kwds` collects all remaining keyword arguments into a dictionary"""
    return args, kwds

print(three(1, 2, 3, butts='www', what=3))
