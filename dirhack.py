def dit(x):
    """Returns `dir(x)`, with the names containing '__' filtered out."""
    return filter(lambda y: True if y.rfind('__') == -1 else False, dir(x))

def ditf(x):
    """Returns the callable non-private properties of `x`"""
    return filter(lambda y: hasattr(x.__getattribute__(y), '__call__'), dit(x))
