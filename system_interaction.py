import os
"""Operating system stuff.
subprocess has newer stuff for process interaction.
"""

import sys
"""Sys has got stuff for interacting with the current python interpreter/program being run?

"""


# Checking the system's python version
if sys.version_info >= (2, 7):
    print('Running python 2.7 or later.')
else:
    print('Python version < 2.7.x')

# You can change `sys.path` at runtime. 
# Shadowing is when one name gets in the way of another name being recognized somewhere else (later in the L(n)GB analysis).
# Shadowing occurs with sys.path as well: the locations are checked in the order they appear in the path-list.

# `sys.argv` => command line arguments given to current python process
# (argv => argument vector; argc => argument count (not needed in python))
# in python len(argv) replaces argc.

"""
ipython is an enhanced python interpreter.
heyooo. It's got all sort of convenient things switched on.
`!(...)` --> (...) gets executed on the underlying shell.
Also commands that aren't recognized as valid in the current python scope are sent to the shel.l
"""
