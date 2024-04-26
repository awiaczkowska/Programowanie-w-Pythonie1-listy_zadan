import unittest
from z2l10 import *

class TestUrn(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
           Urn( [("blue", 1), ("red", -6), ("blue", 2)] )

    def test_add(self):
        a=Urn( [("blue",3)] )
        b=Urn( [("blue",6)] )
        a.add("blue", 3)
        self.assertEqual(a, b)
        c = Urn([("blue", 6), ("red", 3)])
        a.add("red", 3)
        self.assertEqual(a, c)
        x=Urn( [("blue",3)] )
        y=Urn( [("blue",3)] )
        x.add("pink",0)
        y.add("blue",0)
        self.assertEqual(x,y)
        with self.assertRaises(ValueError):
            a.add("purple",-3)

    def test_remove(self):
        a=Urn([("blue", 3), ("red", 3)])
        with self.assertRaises(ValueError):
            a.remove("pink",2)
        with self.assertRaises(ValueError):
            a.remove("red",-2)
        with self.assertRaises(ValueError):
            a.remove("blue", 7)

        a.remove("red",3)
        b=Urn([("blue", 3)])
        self.assertEqual(a,b)
        t = a == b
        self.assertTrue(t)

    def test_get(self):
        d = Urn([("blue", 1), ("red", 3), ("blue", 2)])
        self.assertEqual(d.get("blue"),3)
        self.assertEqual(d.get("pink"), 0)


    def test_transfer(self):
        a=Urn( [("blue", 1)])
        b=Urn( [("blue", 1)])
        with self.assertRaises(ValueError):
           a.transfer(a)
        a.transfer(b)
        c=Urn( [("blue", 2)])
        d=Urn([])

        self.assertEqual(a,d)
        self.assertEqual(b,c)

    def test_draw_chance(self):
        d = Urn([])
        with self.assertRaises(ZeroDivisionError):
           d.draw_chance("pink")
        d.add("pink",2)
        f=Fraction(1)
        self.assertEqual(d.draw_chance("pink"), f)
        f = Fraction(0)
        self.assertEqual(d.draw_chance("black"), f)
        d.add("blue", 8)
        f = Fraction(2,8+2)
        self.assertEqual(d.draw_chance("pink"), f)

    def test_str(self):
        a = Urn([("blue", 2)])
        self.assertEqual(str(a),"{'blue': 2}")

    def test_eq(self):
        b=Urn([("blue",6)])
        c = Urn([("blue", 3), ("red", 3)])
        d=Urn([ ("blue",1),("red", 3),("blue",2) ])
        self.assertEqual(c,d)
        self.assertNotEqual(b,c)

        a = Urn([("red", 3)])
        b = Urn([("red", 3)])
        t = a == b
        self.assertTrue(t)





if __name__ == "__main__":
    unittest.main()
