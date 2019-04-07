import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_last(self):
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_first(self):
        tlist = [3, 2, 1]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_all(self):
        tlist = [0, 0, 0]
        self.assertEqual(max_list_iter(tlist), 0)

    def test_max_list_iter_negative(self):
        tlist = [-2, -1, -3]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_max_list_iter_empty(self):
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)


    def test_reverse_rec_none(self):
        rlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(rlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    def test_reverse_rec_01(self):
        self.assertEqual(reverse_rec([0, 0, 0]),[0, 0, 0])
    def test_reverse_rec_02(self):
        self.assertEqual(reverse_rec([1, 0, 0]),[0, 0, 1])
    def test_reverse_rec_03(self):
        self.assertEqual(reverse_rec([-1, 0, 1]),[1, 0, -1])


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_first(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )

    def test_bin_search_last(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)

    def test_bin_search_not_found(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(15, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_none(self):
        blist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(5, 0, 5, blist)

if __name__ == "__main__":
        unittest.main()

    
