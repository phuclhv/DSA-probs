# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        cur_node = head 
        #create a list of copy pointer
        while cur_node:
            tmp = Node(cur_node.val, cur_node.next, None)
            cur_node.next = tmp
            cur_node = tmp.next
        # 1 1' 2 2' 3 3' 4 4'
        
        #Create the random pointer in each node in copy
        cur_node = head
        while cur_node:
            if cur_node.random:
                cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next
        
        # Reattached the link list
        cur_node = head
        res = head.next
        while cur_node and cur_node.next:
            tmp = cur_node.next
            cur_node.next = cur_node.next.next
            cur_node = tmp
        
        return res