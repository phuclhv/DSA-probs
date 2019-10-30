'''
Given a String s and int r , first fill each character row wise and print column wise.
for e.g. String s = “abcdefgh” and r = 3
so filling column wise would give :
a d g
b e h
c f
'''
class Solution:
  def str_to_col(self, s, row):
    l = len(s)
    for i in range(row):
      idx = i
      while idx < l:
        print(s[idx],end=" ")
        idx += row
      print()
 

test = Solution()
test.str_to_col("abcdefgh", 5)