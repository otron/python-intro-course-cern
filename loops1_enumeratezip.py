zip('butt', [1, 2, 3, 4])

strig = 'what'
for i, c in zip(strig, range(0, len(strig))):
    print(i, c)

def enumerate_c(x):
    return zip(range(len(x)), x)

def forprintcustom(x):
    for i, c in enumerate_c(x):
        print(i, c)

def buttfunc(x):
    """This is the docstring for the buttfunc."""
    pass

forprintcustom('whattt')
