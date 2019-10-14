
'''
Two lists were given. Each list contains elements in the form of an array, [x, y], where x represents the id, and y represents the value. 
Return all pairs with their ids whose sum of values are closest to maxValue, but not greater than maxValue. (Runtime cannot be n^2)
Input:
List1: [[1, 2], [2, 4], [3, 5]]
List2: [[1, 1], [2, 7], [3, 2]]
maxValue: 10

Output:
[[1, 2]]

Input:
List1: [[1, 3], [2, 6], [3, 5]]
List2: [[1, 2], [2, 7], [3, 4]]
maxValue: 10

Output:
[[1, 2], [2, 3]] 
'''
# structure of element in array [IDX, VALUE]
IDX = 0
VALUE = 1

def max_values(arr1, arr2, target):

  # largest value of a pair that is less than target 
  max_sum_pair = -float("inf")
  # Store pairs that have sum = max_sum
  max_arr = []
  
  
  # Sort 2 array based on their value
  arr1.sort(key=lambda x: x[VALUE])
  arr2.sort(key=lambda x: x[VALUE])
  
  # Return index of largest value that is less or equal than @num_find in @array
  def closest_bi_search(array, num_find):
    low, high = 0, len(array)-1
    while low <= high:
      if array[high][1] < num_find:
        return high
      mid = low + (high - low) // 2
      if array[mid][1] == num_find:
        return mid
      if array[mid][1] < num_find:
        low = mid + 1
      else:
        high = mid - 1
    return high

  # Iterate for every @element in first array. Form of @element [idx,value]
  # Binary search in arr2 for the index for the value that form the largest sum less than @target
  for element in arr1:
    closest_idx = closest_bi_search(arr2, target - element[VALUE])    
    curr_sum_pair = element[VALUE] + arr2[closest_idx][VALUE]

    # If curr_sum_pair > max_sum_pair, register new max_sum_pair, reset max_arr and add the pair to max_arr
    # If curr_sum_pair == max_sum_pair, add the pair to max_arr
    if curr_sum_pair > max_sum_pair:
      max_sum_pair = curr_sum_pair
      max_arr = []
      max_arr.append([element[IDX], arr2[closest_idx][IDX]])
    elif curr_sum_pair == max_sum_pair:
      max_arr.append([element[IDX], arr2[closest_idx][IDX]])

  return max_arr

print(max_values([[1, 2], [2, 4], [3, 5]], [[1, 1], [2, 7], [3, 2]],10))
print(max_values([[1, 3], [2, 6], [3, 5]],[[1, 2], [2, 7], [3, 4]],10))
