a = 5
def foo():
    print a
    a = 3

foo()
# Results in an UnboundLocalError in python 2.7.x because `a`
# is a local variable/binding in the local scope of `foo` 
# This makes fancy closures like:
# def whut(x):
#     def yes():
#         print(x)
#         x += 1
#     return yes

# Impossible without some hack (like storing the variable in a list or something
# equally mutable).
