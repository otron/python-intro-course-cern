from __future__ import print_function
import unittest
import pqueue
from pqueue import EmptyQueue

# This test suite consists of 5 tests, which test the semantic
# behaviour of the implementation. These tests are switched on by
# default. A further 3 tests (conributed by Jan Iven) exist
# for testing the speed of the implementation.  The performance tests
# are switched off by default; to enable the performance tests, pass a
# time limit (in seconds) as a command-line argument


# Main body of the test suite starts here
class queue_test(unittest.TestCase):

    def setUp(self):
        self.q = pqueue.priority_queue()

    def testEmptyQueue(self):
        "Popping from empty queue should raise EmptyQueue"
        self.assertRaises(EmptyQueue, self.q.pop)

    def testDefaultPriority(self):
        "Default priority should be 2"
        self.q.add('first in')
        self.q.add('second in', 1)
        self.q.add('third in')
        self.assertEqual(self.q.pop(), 'second in')
        self.assertEqual(self.q.pop(), 'first in')
        self.assertEqual(self.q.pop(), 'third in')
        self.q.add('fourth in')
        self.q.add('fifth in', 3)
        self.q.add('sixth in')
        self.assertEqual(self.q.pop(), 'fourth in')
        self.assertEqual(self.q.pop(), 'sixth in')
        self.assertEqual(self.q.pop(), 'fifth in')

    def testPriorityOutOfRange(self):
        "Submitting an out-of-range priority should raise ValueError"
        self.assertRaises(ValueError, self.q.add, 'dummy',  5)
        self.assertRaises(ValueError, self.q.add, 'dummy', -1)

    def testPriorityWrongType(self):
        "Submitting a non-int priority should raise TypeError"
        self.assertRaises(TypeError, self.q.add, 'dummy', 1.1)

    def testPriority(self):
        "The priorities should be respected"
        self.q.add(10,2)
        self.q.add(9,1)
        self.q.add(8,1)
        self.q.add(7,2)
        self.q.add(6,4)
        self.q.add(1,3)
        self.q.add(2,4)
        self.q.add(3,0)
        self.q.add(4,0)
        self.q.add(5,3)
        out = (self.q.pop(), self.q.pop(), self.q.pop(), self.q.pop(), self.q.pop(),
               self.q.pop(), self.q.pop(), self.q.pop(), self.q.pop(), self.q.pop())
        self.assertEqual(out, (3,4,9,8,10,7,1,5,6,2))

    # This is the same test as above, refactored to be a bit less
    # verbose. Note that the names of both methods are identical,
    # thererfore the second one will displace the first one.
    def testPriority(self):
        "The priorities should be respected"
        for object, priority in ((10,2),
                                 (9,1),
                                 (8,1),
                                 (7,2),
                                 (6,4),
                                 (1,3),
                                 (2,4),
                                 (3,0),
                                 (4,0),
                                 (5,3)):
            self.q.add(object, priority)

        out = [self.q.pop() for _ in range(10)]
        self.assertEqual(out, [3,4,9,8,10,7,1,5,6,2])

    def testLen(self):
        "len(queue) should return the number of items in the queue."
        self.assertEqual(len(self.q), 0)
        self.q.add(1)
        self.assertEqual(len(self.q), 1)
        self.q.add(2)
        self.assertEqual(len(self.q), 2)
        self.q.add(3,1)
        self.assertEqual(len(self.q), 3)
        self.q.add(4,2)
        self.assertEqual(len(self.q), 4)
        self.q.add(5,0)
        self.assertEqual(len(self.q), 5)
        self.q.pop()
        self.assertEqual(len(self.q), 4)
        self.q.pop()
        self.assertEqual(len(self.q), 3)
        self.q.add(6)
        self.assertEqual(len(self.q), 4)
        self.q.add(7,3)
        self.assertEqual(len(self.q), 5)
        self.q.add(8,1)
        self.assertEqual(len(self.q), 6)
        self.q.pop()
        self.assertEqual(len(self.q), 5)

    # This is the same test as above, refactored to be a bit more
    # legible. Note that the names of both methods are identical,
    # thererfore the second one will displace the first one.
    def testLen(self):
        "len(queue) should return the number of items in the queue."
        len_should_now_be = lambda n:self.assertEqual(len(self.q),n)
        add = self.q.add
        pop = self.q.pop

        pass;     len_should_now_be(0)
        add(1);   len_should_now_be(1)
        add(2);   len_should_now_be(2)
        add(3,1); len_should_now_be(3)
        add(4,2); len_should_now_be(4)
        add(5,0); len_should_now_be(5)
        pop();    len_should_now_be(4)
        pop();    len_should_now_be(3)
        add(6);   len_should_now_be(4)
        add(7,3); len_should_now_be(5)
        add(8,1); len_should_now_be(6)
        pop();    len_should_now_be(5)




########################################################################
# End of semantic tests. Ignore the rest of this file until you pass
# the five tests above.
########################################################################
prefix = 'priority_queue_'
implementations = [name.replace(prefix,'') for name in dir(pqueue)
                   if name.startswith(prefix)]

import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--alt",   choices=implementations,
                  help="Test alternative implementation priority_queue_<ALT>")
parser.add_option("-t", "--time",  type="float",
                  help="Switch on timing tests. Test fails after TIME")
parser.add_option('-n',            type="int",
                  help="Number of elements to process in the speed test",
                  default=50000)
parser.add_option(      "--teeth", type="int", default=100,
                        help="Number of teeth to use in the sawtooth speed test")

options, args = parser.parse_args()

# ----------------------------------------------------------------------
if options.alt:
    name = "priority_queue_" + options.alt
    pqueue.priority_queue = getattr(pqueue, name)
# ----------------------------------------------------------------------


# Performance testing prelude ...

# These tests rely on Unix-only functions in the signal module (so
# they will not work on Windows). These functions do not accept
# fractions of seconds, but on fast machines the tests complete in
# under a second, so I added the ability to specify fractions of
# seconds as the time limit.


print("\nImplementation used:", pqueue.priority_queue.__name__)

if options.time:
    fine_time_limit = options.time
    print("Speed tests switched on.")
    print("Time limit = %.1f s" % fine_time_limit)
    print("Processing %d elements, in %d teeth." % (options.n, options.teeth))
    import math
    time_limit = int(math.ceil(fine_time_limit)) # round up; signal takes integers
    fine_time_limit *= 1000 # Convert to milliseconds
    import signal
    import time
else:
    print("Speed tests switched off.")
    print("To enable speed tests, use the '-t TIME' option, where TIME")
    print("is the time limit per test, in seconds.")
    time_limit = False

# NB: The performance tests are off by default.
def mytimer(sig, stack):
    raise TimerExpired

class TimerExpired(Exception):
    pass

time_reports = []
# End of performance-testing prelude.

# ----------------------------------------------------------------------

if time_limit:
    # Thanks to Jan Iven for contributing the following timing tests.
    class queue_test_speed(unittest.TestCase):

        def setUp(self):
            self.q = pqueue.priority_queue()

        def makeTest(action):
            def test(self):
                oldsignal=signal.signal(signal.SIGALRM, mytimer)
                signal.alarm(time_limit)
                try:
                    start = time.time()
                    action(self)
                    time_taken = time.time() -start
                except TimerExpired:
                    self.fail("timeout after %.1f seconds" % time_limit)
                signal.signal(signal.SIGALRM, oldsignal)
                self.assertTrue(time_taken < fine_time_limit)
                time_reports.append("%-8s test completed in %.3f seconds" %
                                    (action.__name__[4:].capitalize(), time_taken))
            test.__doc__ = action.__doc__
            return test

        @makeTest
        def testTriangle(self):
            """check performance of the implementation. Triangle pattern
            50000 add(), 50000 pop(), equally distributed over priorities"""

            for i in range(options.n):
                self.q.add(i,i%5)
            for i in range(options.n):
                self.q.pop()

        @makeTest
        def testSawtooth(self):
            """check performance of the implementation. Sawtooth pattern
            500x(100 add(), 100 pop()), equally distributed over priorities"""

            per_tooth = options.n // options.teeth
            for i in range(options.teeth):
                for j in range(per_tooth):
                    self.q.add(i,i%5)
                for j in range(per_tooth):
                    self.q.pop()

        @makeTest
        def testFlat(self):
            """check performance of the implementation. Flat pattern
            50000 add()/pop(), equally distributed over priorities"""

            for i in range(options.n):
                self.q.add(i,i%5)
                self.q.pop()

        @makeTest
        def testPlateau(self):
            # This test was inspired by a discussion with Markus Elsing
            """check performance of the implementation. Plateau pattern
            N x add(), N x (add(), pop()), N x pop()"""
            for i in range(options.n//2):
                self.q.add(i,i%5)
            for i in range(options.n//2):
                self.q.add(i,i%5)
                self.q.pop()
            for i in range(options.n//2):
                self.q.pop()


# ----------------------------------------------------------------------

# Unittest does not expect to find the extra parameters we pass (time
# limit, implementation). Remove them before running unittest.
sys.argv = sys.argv[:1]

try:
    # unittest shuts down the interpreter when it finishes the
    # tests. We want to delay the exit, in order to display some
    # timing information, so we handle the SystemExit exception.
    unittest.main()
except SystemExit:
    if time_reports:
        print
        for r in time_reports:
            print(r)


# Changelog

# replaced use of deprecated (and removed in Python 2.5) timing
# module, with time module (jacek 17/10/2006)
