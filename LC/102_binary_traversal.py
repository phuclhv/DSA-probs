# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def levelOrder(self, root) -> int:
    nodes_in_level = []
      
    def dfs(node, level):
      if not node:
        return
      nonlocal nodes_in_level
        
      if level >= len(nodes_in_level):
          nodes_in_level.append([])
          
      nodes_in_level[level].append(node.val)
      dfs(node.left, level + 1)
      dfs(node.right, level + 1)
    
    dfs(root,0)
    
    return nodes_in_level