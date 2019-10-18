'''
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.
Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.
If the task is impossible, return -1.

Examples:

source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]

output: -1

Constraints:

    [time limit] 5000ms
    [input] string source
        1 ≤ source.length ≤ 20
    [input] string target
        1 ≤ target.length ≤ 20
    [input] array.string words
        1 ≤ words.length ≤ 20
    [output] array.integer

'''
from collections import defaultdict
def shortestWordEditPath(source, target, words):
  if target not in words:
    return -1
  
  def diff_in_one_char(word1, word2):
    if len(word1) != len(word2):
      return False
    count_diff = 0
    for idx, char in enumerate(word1):
      if word2[idx] != char:
        count_diff += 1
    return count_diff == 1
  
  jump_list = defaultdict(set)

  for i in range(len(words)):
    for j in range(i+1,len(words)):
      if diff_in_one_char(words[i], words[j]):
        jump_list[i].add(j)
        jump_list[j].add(i)   
  
  def dfs(index, step, min_step, marked):
    marked[index] = True
    if words[index] == target:
      min_step = min(min_step, step+1)
      return min_step
    for idx in jump_list[index]:
      if not marked[idx]:
        min_step = min(min_step,dfs(idx, step+1, min_step, marked))
        marked[idx] = False
    return min_step
  
  #print(jump_list)
  min_step = float("inf")
  for i in range(len(words)):
    marked = [False for x in range(len(words))]
    if diff_in_one_char(source, words[i]):
      min_step = min(min_step,dfs(i,0, min_step,marked))
    print(min_step)

  #print(min_step)
  return min_step if min_step != float("inf") else -1

source, target = "bit", "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortestWordEditPath(source, target, words))

source, target = "no", "go"
words = ["to"]
print(shortestWordEditPath(source, target, words))