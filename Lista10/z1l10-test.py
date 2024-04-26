import unittest
from z1l10 import *
class TestPolynomial(unittest.TestCase):
    def test_init(self):
        a=Polynomial([])
        b=Polynomial([0])
        self.assertEqual(a,b)
        
    def test_deg(self):
        self.assertEqual(  Polynomial([0,1,2,3,4,5,0,0,0]).deg() , 5 )

    def test_str (self):
        self.assertTrue( str(Polynomial([1,1,0,-2,3,0]))=="1 + 1 x^1 + 0 x^2 - 2 x^3 + 3 x^4")

    def test_eq(self):
        a=Polynomial([0,1,-2,3,4,5])
        b=Polynomial([0,1,-2,3,4,5])
        #self.assertTrue( a==b)
        self.assertEqual(a,b)

    def test_neg(self):
        a=Polynomial([0, 1, -2])
        b=Polynomial([0,-1,2])
        self.assertEqual(-a,b )

    def test_add(self):
        lst = [1, 1, 0, -2, 3, 0]
        x = Polynomial(lst)
        y = Polynomial([0, 0, 1000])
        self.assertEqual( x+y, Polynomial([1, 1, 1000, -2, 3]) )

    def test_sub(self):
        lst = [1, 1, 0, -2,3]
        a=Polynomial(lst)
        l=[1,1,0]
        b=Polynomial(l)
        c=Polynomial([0,0,0,-2,3])
        self.assertEqual(a-b,c)

    def test_mull(self):
        a = Polynomial([1])
        b = Polynomial([0, 1])
        c=Polynomial([0,-20])
        d=Polynomial([0,0,-20])
        self.assertEqual(a*b,b)
        self.assertEqual(c * b, d)

    def test_call(self):
        lst = [1, 1, 0, -2, 3, 0]
        x = Polynomial(lst)
        self.assertEqual(x(0), 1)
        y=Polynomial([0,-20])
        self.assertEqual(y(1), -20)


if __name__=="__main__":
    unittest.main()
