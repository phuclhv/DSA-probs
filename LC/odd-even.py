import random
max_sum = -float('inf')
seq = '' 
def odd_even(list_arr, sumArray, sequence):
    global max_sum,seq
    if len(list_arr) == 0:
        if sumArray > max_sum:
            max_sum = sumArray
            seq = sequence
    else:
        odd_even(list_arr[1:],sumArray + sum(list_arr),sequence + '1L ')
        odd_even(list_arr[:-1],sumArray + sum(list_arr), sequence + '1R ')
        odd_even(list_arr[1:],sumArray - sum(list_arr), sequence + '2L ')
        odd_even(list_arr[:-1],sumArray - sum(list_arr), sequence + '2R ')
    
def dp_odd_even(list_arr):
    len_list = len(list_arr)
    max_sum = [[0 for x in range(len_list)] for y in range(len_list)]
    for i in range(len_list):
        for j in range(len_list):
            max_sum[i][j] = max(sum(list_arr[i:j+1]),-sum(list_arr[i:j+1]))
    
    target_row, target_col = 0,len_list-1
    result = -float('inf')
    for i in range(len_list):
        max_sum_end_with_i = max_sum[i][i]
        row, col = i,i
        while row != target_row or col != target_col:
            if row <= target_row:
                col += 1
                max_sum_end_with_i += max_sum[row][col]
            elif col >= target_col or max_sum[row-1][col] > max_sum[row][col+1]:
                row -= 1
                max_sum_end_with_i += max_sum[row][col]
            else:
                col += 1
                max_sum_end_with_i += max_sum[row][col]
        result = max(result, max_sum_end_with_i)

    return result
     

list = [1,2,3,4]
odd_even(list,0,'')
print(dp_odd_even(list))
print(max_sum, seq)

max_sum = -float('inf')
seq = '' 
list = [-1,-2,-3,-4]
odd_even(list,0,'')
print(dp_odd_even(list))
print(max_sum, seq)


max_sum = -float('inf')
seq = '' 
list = [-1,-2,-3,-4,4,-6,-100,10]
odd_even(list,0,'')
print(dp_odd_even(list))
print(max_sum, seq)


max_sum = -float('inf')
seq = '' 
list = [random.randint(-100, 100) for x in range(1000)]
#odd_even(list,0,'')
print(dp_odd_even(list))
#print(max_sum, seq)
