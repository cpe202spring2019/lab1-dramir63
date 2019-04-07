import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location(SLO, 35.3, -120.7)")
        #print("done")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("LA", 34.0, 118.24)
        self.assertEqual(loc, loc2)
        self.assertIsNot(loc, loc3)
        #print("done")
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
