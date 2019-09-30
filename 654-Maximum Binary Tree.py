class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))

    def construct(self, nums: List[int], L: int, R: int) -> TreeNode:
        if L == R:
            return None
        max_i = self.findMax(nums, L, R)
        root = TreeNode(nums[max_i])
        root.left = self.construct(nums, L, max_i)
        root.right = self.construct(nums, max_i + 1, R)
        return root

    def findMax(self, nums: List[int], L:int, R:int) -> TreeNode:
        max_i = L
        for i in range(L,R):
            if nums[max_i] < nums[i]:
                max_i = i
        return max_i