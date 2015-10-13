import operator
def sumfile(fname):
    with open(fname, 'r') as f:
        return [reduce(operator.add,
                       map(int,
                           line.strip().split()), 0)
                for line in f]


print(sumfile('numbs'))

def sumfile_ignore(fname):
    res = []
    with open(fname) as f:
        for line in f:
            # split each line into separate tokens
            tokens = line.strip().split()
            # filter out non-numbers
            numbers_str = filter(str.isdigit, tokens)
            # convert to integers
            numbers = map(int, numbers_str)
            # add 'em up
            res.append(reduce(operator.add, numbers, 0))
    return res
            
print(sumfile_ignore('numbs2'))

def tryfunc(x):
    res = 0
    try:
        res = int(x)
    except ValueError as e:
        pass
    finally:
        return res

def sumfile_ignore_except(fname):
    res = []
    with open(fname) as f:
        for line in f:
            # split each line into separate tokens
            tokens = line.strip().split()
            # filter out non-numbers
            # convert to integers
            numbers = map(tryfunc, tokens)
            # add 'em up
            res.append(reduce(operator.add, numbers, 0))
    return res

print(sumfile_ignore_except('numbs2'))
