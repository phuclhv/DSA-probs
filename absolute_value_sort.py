'''
Absolute Value Sort

Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr. If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]

Constraints:

    [time limit] 5000ms
    [input] array.integer arr
        0 ≤ arr.length ≤ 10
    [output] array.integer

'''
from functools import cmp_to_key
def absSort(arr):
  def compare_abs(value1, value2):
    if abs(value1) <= abs(value2):
      return -1
    return 1
    
  compare_abs_key = cmp_to_key(compare_abs)
  arr.sort(key=compare_abs_key)
  
  return arr

arr = [2, -7, -2, -2, 0]
print(absSort(arr))