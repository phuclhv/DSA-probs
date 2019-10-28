# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root) -> int:
        if not root:
            return []
        nodes_in_level = []
      
        def bfs(nodes):
            nonlocal nodes_in_level
            
            nodes_in_nex_level = []
            vals_in_cur_level = []
            
            for node in nodes:
                vals_in_cur_level.append(node.val)
                if len(nodes_in_level) % 2 == 0:
                    if node.left:
                        nodes_in_nex_level.append(node.left)
                    if node.right:
                        nodes_in_nex_level.append(node.right)
                else:
                    if node.right:
                        nodes_in_nex_level.append(node.right)
                    if node.left:
                        nodes_in_nex_level.append(node.left)
            
            nodes_in_level.append(vals_in_cur_level)
            if len(nodes_in_nex_level) > 0:
                bfs(nodes_in_nex_level[::-1])
        
        bfs([root])
        
        return nodes_in_level
        
        