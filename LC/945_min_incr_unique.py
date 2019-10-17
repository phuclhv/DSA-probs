'''
https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

 

Note:

    0 <= A.length <= 40000
    0 <= A[i] < 40000

'''

class Solution:
    def minIncrementForUnique(self, A):
        A.sort()
        idx = 1
        min_increment = 0
        
        def sum_from_1_to_num(num):
            return (num * (num +1))//2
        
        same_num = 0
        
        while idx < len(A):
            while A[idx] == A[idx-1]:
                same_num +=1
                idx +=1
                if idx >= len(A):
                    return (min_increment + sum_from_1_to_num(same_num))
            if same_num != 0:
                diff = A[idx] - A[idx-1]
                if diff > same_num:
                    min_increment += sum_from_1_to_num(same_num)
                    same_num = 0
                else:
                    min_increment += sum_from_1_to_num(diff) + (same_num-diff)*diff
                    same_num = same_num - diff + 1
            idx +=1
            
            
        return (min_increment + sum_from_1_to_num(same_num))
                