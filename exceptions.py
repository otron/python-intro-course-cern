"""
Exceptions are...

1. Messages from the top of the stack to anyone who cares lower down along the stack.

2. An alternative channel for data for data flow out of functions.
(alternative to return)

3. Branching mechanism


try:
    # Code to 'try'
except UnboundLocalError:
    # What to do if UnboundLocalError.
except IndexError, whut:
    # `whut` binds to the exception
except:
    # catch-all for any kind of error/exception (don't use this, says Jacek).
else:  # optional
    # what to do if no exception was raised

try:
    # code.
finally:
    # what to do always, yo


else has to follow an except.

except (A,B):  # listening for exceptions of type A or B.
except A, B:  # listening for exceptions of type A which will be bound to the name `B`

new syntax:
except Exception as e:
# equivalent to `except (Exception,), e`?
"""
