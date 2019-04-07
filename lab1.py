
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
  # pass
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   max = int_list[0]
   for x in int_list:
      if x > max:
         max = x
   return max

def reverse_rec(int_list):   # must use recursion
   #"""recursively reverses a list of numbers and returns the reversed list
   #If list is None, raises ValueError"""
   #pass
    if int_list == None:
        raise ValueError
    if not int_list:
      return int_list
    return int_list[-1:] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   #pass
   if int_list == None:
      raise ValueError
   middle = (low + high) // 2
   if target == int_list[middle]:
      return int_list.index(target)
   if high >= low:
       if target < int_list[middle]:
          return bin_search(target, low, middle - 1, int_list)
       if target > int_list[middle]:
          return bin_search(target, middle + 1, high, int_list)
   return None
