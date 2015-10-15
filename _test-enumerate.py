import unittest

import enumerate as implementation

class test_enumerate(unittest.TestCase):

    enumerate = staticmethod(enumerate)

    def setUp(self):
        self.data = "hello"

    def test_values(self):
        self.assertEqual(list(self.enumerate(self.data)),
                         list(     enumerate(self.data)))

    def test_optional_argument(self):
        start = 3
        self.assertEqual(list(self.enumerate(self.data, start)),
                         list(     enumerate(self.data, start)))
    
    def test_has_next(self):
        e,m = enumerate(self.data), self.enumerate(self.data)
        while True:
            try:
                assert e.next() == m.next()
            except StopIteration:
                break

    def test_is_iterable(self):
        i = self.enumerate(iter(self.data))
        i.next()

    def test_laziness(self):

        class MyMessage(Exception):
            pass

        def blows_up_on_third():
            yield 1
            yield 2
            raise MyMessage

        iterator = iter(self.enumerate(blows_up_on_third()))
        self.assertEqual(next(iterator), (0,1))
        self.assertEqual(next(iterator), (1,2))
        self.assertRaises(MyMessage, next, iterator)
        
class test_genumerate(test_enumerate):

    enumerate = staticmethod(implementation.genumerate)

class test_ienumerate(test_enumerate):

    enumerate = staticmethod(implementation.ienumerate)
    
class test_cenumerate(test_enumerate):

    enumerate = staticmethod(implementation.cenumerate)

if __name__ == '__main__':
    unittest.main()
