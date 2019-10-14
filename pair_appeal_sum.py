'''
Find Pair With Max Appeal Sum
Input: Array
Output: index {i, j} ( i = j allowed) with maximum Appeal
Appeal = A[i] +A[j] + abs(i-j)

Example 1:

Input: [1, 3, -1]
Output: [1, 1]
Explanation: Appeal = A[1] + A[1] + abs(0) = 3 + 3 + 0 = 6
Example 2:

Input: [1, 6, 1, 1, 1, 1, 7]
Output: [1, 6]
Explanation 6 + 7 + abs(1 - 6) = 18
Example 3:

Input: [6, 2, 7, 4, 4, 1, 6]
Output: [0, 6]
Explanation: 6 + 6 + abs(0 - 6) = 18
'''

def pair(arr):
  if not arr:
    return None
  res = [0,0]
  max_idx_so_far, max_value_so_far, max_pair = 0, arr[0], arr[0] * 2
  for idx, element in enumerate(arr):

    if element - idx > max_value_so_far:
      max_idx_so_far, max_value_so_far = idx, element-idx

    if element + arr[max_idx_so_far] + abs(idx - max_idx_so_far) > max_pair:
      max_pair = element + arr[max_idx_so_far] + abs(idx - max_idx_so_far)
      res = [max_idx_so_far,idx]

  return res
    
print(pair([1,3,1]))
print(pair([1,6,1,1,1,1,7]))
print(pair([6,2,7,4,4,1,6]))
print(pair([]))