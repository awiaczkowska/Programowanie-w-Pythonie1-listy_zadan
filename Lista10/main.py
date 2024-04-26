import unittest

# upper, isupper, split
'''class TestString(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("Foobar".upper(), "FOOBAR")
        self.assertNotEqual("Foobar".upper(), "FOOBAR2")

    def test_isupper(self):
        self.assertTrue("FOOBAR".isupper())
        self.assertFalse("Foobar".isupper())

    def test_split(self):
        self.assertEqual("abc def".split(), ["abc", "def"])
        self.assertIn("abc", "abc def".split())
        with self.assertRaises(TypeError):
            "abc def".split(2)'''

if __name__ == '__main__':
    #unittest.main()
    d1={1:'a',2:0}
    d2={2:0, 1:"a"}
    print(d1==d2)
    del(d2[2]); del(d2[1])
    print(d2)
    d=dict( [ ("blue",1),("red", 3),("blue",2) ])
    print (d)
    del(d1)
    print(len(d2))
