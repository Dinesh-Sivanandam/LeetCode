# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        elif n == 2:
            root = TreeNode(nums[0])
            right = TreeNode(nums[1])
            root.right = right
            return root
        mid = n / 2
        root = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        root.left = left
        root.right = right
        return root
    