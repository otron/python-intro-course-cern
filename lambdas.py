a1 = map(lambda a: a+1, range(1,5))
a2 = filter(lambda x: x%2, range(20))

a = map(lambda *args: args, 'apple', 'mango', 'xxxxx')
ac = map(None, 'apple', 'mango', 'xxxxx')

# returns a list of the odd integers in [0, 19]
b1 = filter(lambda x: x%2, range(20))

c1 = reduce(lambda a,b: a+b, range(10))

c2 = reduce(lambda a,b: a*b, range(1, 101))  # factorial of 100

import operator
truu = c2 == reduce(operator.mul, range(1, 101)) == reduce(operator.mul, map(lambda x: x+1, range(100)))\
          == reduce(operator.mul, range(101)[1:])
