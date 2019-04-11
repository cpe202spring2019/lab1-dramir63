import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #Test if list is None
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_last(self):
        # Test if last number is max
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_first(self):
        # Test if first number is max
        tlist = [3, 2, 1]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_iter_all(self):
        # Test max if all numbers are the same
        tlist = [0, 0, 0]
        self.assertEqual(max_list_iter(tlist), 0)

    def test_max_list_iter_negative(self):
        # Test if numbers in list are negative
        tlist = [-2, -1, -3]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_max_list_iter_empty(self):
        # Test if list is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)


    #def test_max_list_iter_bug(self):
      #  #Test for bug / failure:
       # blist = ["string", "bug"]
       # self.assertEqual(max_list_iter(blist), None)

    def test_reverse_rec_none(self):
        # Test if list is None
        rlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(rlist)


    def test_reverse_rec(self):
        # Test if function works as intended
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])


    def test_reverse_rec_all(self):
        # Test if all numbers in list are same
        self.assertEqual(reverse_rec([0, 0, 0]),[0, 0, 0])


    def test_reverse_rec_02(self):
        # Test if all but two numbers are the same
        self.assertEqual(reverse_rec([1, 0, 0]),[0, 0, 1])


    def test_reverse_rec_negative(self):
        # Test if list has a negative number
        self.assertEqual(reverse_rec([-1, 0, 1]),[1, 0, -1])


    def test_bin_search(self):
        # Test if functions works as intended
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )


    def test_bin_search_first(self):
        # Test if target is first number in list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )



    def test_bin_search_last(self):
        # Test if target is last number in list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)


    def test_bin_search_not_found(self):
        # Test if target is not found
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(15, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_out(self):
        #Test if value is out of index bounds
        list_val = [0, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(1, low, high, list_val), None)

    def test_bin_search_none(self):
        # Test if list is None
        blist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(5, 0, 5, blist)



if __name__ == "__main__":
        unittest.main()

    
