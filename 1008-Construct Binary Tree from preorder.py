class Solution(object):
    idx = 0
    def bstFromPreorder(self, preorder):
        if not preorder:
            return

        return self.helper(-float('inf'), float('inf'), preorder)

    def helper(self, lower, upper, nums):
        if self.idx == len(nums):
            return None
        val = nums[self.idx]
        if val < lower or val > upper:
            return None

        root = TreeNode(val)
        self.idx += 1
        root.left = self.helper(lower, val, nums)
        root.right = self.helper(val, upper, nums)
        return root