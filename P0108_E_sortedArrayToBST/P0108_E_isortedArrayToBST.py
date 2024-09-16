# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        
        left = 0
        right = len(nums)
        mid = (left+right)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[left:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:right])
        return root