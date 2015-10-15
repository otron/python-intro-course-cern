from __future__ import print_function
from unittest import TestCase, main
from memoization import fib, memo, time
from time import sleep

class Test(TestCase):

    def test_time(self):
        for s in (0.1, 0.4, 0.5, 1.3):
            t, r = time(sleep, s)
            self.assertTrue(s-0.05 < t < s+0.05)

    def test_fib(self):
        for n, f in ((0,1),
                     (1,1),
                     (4,5),
                     (6,13),
                     (7,21)):
            self.assertEqual(fib(n), f)

    def test_memo_on_fib(self):
        Qs = (30, 28, 27, 26, 25)
        mfib = memo(fib)
        for Q in Qs:
            t1, A1 = time( fib, Q)
            t2, A2 = time(mfib, Q)
            # mfib gives the correct answer
            self.assertEqual(A1, A2)
            # mfib takes as long as fib the first time around
            self.assertTrue(0.9 < t1/t2 < 1.1)

            t3, A3 = time(mfib, Q)
            # mfib gives the correct answer the second time around
            self.assertEqual(A1, A3)
            # mfib is much faster the second time around
            self.assertTrue(t3 == 0 or t1/t3 > 10000)
    

    def test_memo_independence(self):
        from operator import add, sub
        madd = memo(add)
        msub = memo(sub)
        for a in range(10):
            for b in range(10):
                self.assertEqual(madd(a,b), add(a,b))
                self.assertEqual(msub(a,b), sub(a,b))

main()
