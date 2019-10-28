# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def zigzagLevelOrder(self, root) -> int:
    nodes_in_level = []
  
    def dfs(node, level):
      if not node:
        return
      nonlocal nodes_in_level
      
      if level >= len(nodes_in_level):
        nodes_in_level.append([])
          
      nodes_in_level[level].append(node.val)
      if level % 2 == 1:
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
      else:
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
            
    dfs(root,0)
      
    return nodes_in_level
      
        