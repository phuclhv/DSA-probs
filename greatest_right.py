'''
You are given an array A of size N. 
Replace every element with the next greatest element (greatest element on its right side) in the array.
'''

class Solution:
  def greater_on_right(self, arr):
    if arr:  
      greatest = arr[-1]
      for idx in range(len(arr)-1, -1,-1):
        if arr[idx] < greatest:
          arr[idx] = greatest
    return arr

test = Solution()
print(test.greater_on_right([16, 17, 4, 3, 5, 2]))
print(test.greater_on_right([2, 3, 1, 9]))


