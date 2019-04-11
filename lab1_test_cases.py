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

    def test_max_list_iter_beg_end(self):
        #Test if number is at beginning and end
        test_list = [4, 1, 4]
        self.assertEqual(max_list_iter(test_list), 4)

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

    def test_max_list_iter_solo(self):
        #Test with list of one element
        one = [5]
        self.assertEqual(max_list_iter(one), 5)

    def test_max_list_iter_negative(self):
        # Test if numbers in list are negative
        tlist = [-2, -1, -3]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_max_list_iter_regular(self):
        #Test regular functionality of function
        self.assertEqual(max_list_iter([1, 2, 3, 8, 5, 7]), 8)
        self.assertEqual(max_list_iter([9, 2, 3, 8, 5, 7]), 9)
        self.assertEqual(max_list_iter([1, 9, 3, 8, 5, 7]), 9)
        self.assertEqual(max_list_iter([1, 2, 9, 8, 5, 7]), 9)
        self.assertEqual(max_list_iter([1, 2, 3, 19, 5, 7]), 19)
        self.assertEqual(max_list_iter([1, 2, 3, 8, 9, 7]), 9)
        self.assertEqual(max_list_iter([1, 2, 3, 8, 7, 19]), 19)

    def test_max_list_iter_empty(self):
        # Test if list is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)



    def test_reverse_rec_solo(self):
        #Test with list of one item
        self.assertEqual(reverse_rec([3]),[3])


    def test_reverse_rec_none(self):
        # Test if list is None
        rlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(rlist)


    def test_reverse_rec(self):
        # Test if function works as intended
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_dups(self):
        #Test if list has duplicates
        self.assertEqual(reverse_rec([3, 4, 4]), [4, 4, 3])


    def test_reverse_rec_all(self):
        # Test if all numbers in list are same
        self.assertEqual(reverse_rec([0, 0, 0]),[0, 0, 0])


    def test_reverse_rec_02(self):
        # Test if all but two numbers are the same
        self.assertEqual(reverse_rec([1, 0, 0]),[0, 0, 1])

    def test_reverse_rec_blank(self):
        #Test if list is blank
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_negative(self):
        # Test if list has a negative number
        self.assertEqual(reverse_rec([-1, 0, 1]),[1, 0, -1])


    def test_reverse_rec_regular(self):
        #Test basic functionality of code
        self.assertEqual(reverse_rec([1, 2, 3, 5]), [5, 3, 2, 1])
        self.assertEqual(reverse_rec([2, 1, 3, 5]), [5, 3, 1, 2])
        self.assertEqual(reverse_rec([5, 3, 2, 1]), [1, 2, 3, 5])
        self.assertEqual(reverse_rec([3, 1, 2, 5]), [5, 2, 1, 3])

    def test_bin_search(self):
        # Test if functions works as intended(+lower end)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 3)
        self.assertEqual(bin_search(5, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val), 5)
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)
        self.assertEqual(bin_search(9, 0, len(list_val) - 1, list_val), 7)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)

    def test_bin_search_higher_quart(self):
        #Test if number is on high end of list
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)


    def test_bin_search_same(self):
        #Test if high and low are the same:
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(3, 1, 1, list_val), None)

    def test_bin_search_low(self):
        # Test if low is higher than high
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(3, 7, 4, list_val), None)


    def test_bin_search_first(self):
        # Test if target is first number in list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )


    def test_bin_search_empty(self):
        #Test if list is empty
        list_val = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), None)


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

    def test_bin_search_solo(self):
        #Test with list with one element
        solo = [2]
        self.assertEqual(bin_search(1, 0, len(solo) - 1, solo), None)
        self.assertEqual(bin_search(2, 0, len(solo), solo), 0)



if __name__ == "__main__":
        unittest.main()

    
