from z2l13 import *
import unittest

class Test_Queue(unittest.TestCase):
    def test_init(self):
        a=Queue()
        self.assertEqual(a.q,[])
        lst=[1,2,3]
        b=Queue(lst)
        lst.append(5)
        self.assertNotEqual(b.q,lst)

    def test_push_back(self):
        lst = [1, 2, 3]
        b = Queue(lst)
        b.push_back(6)
        self.assertEqual([1,2,3,6], b.q)

    def test_empty(self):
        self.assertTrue( (Queue().empty()) )
        self.assertFalse((Queue([1,2,3]).empty()))

    def test_pop_front(self):
        lst = [1, 2, 3]
        b = Queue(lst)
        self.assertEqual( b.pop_front(),1)
        self.assertEqual(b.q,[2,3])

    def test_front(self):
        lst = [6, 2, 3]
        b = Queue(lst)
        self.assertEqual(b.front(), 6)
        self.assertEqual(lst, b.q)

if __name__=="__main__":
    unittest.main()