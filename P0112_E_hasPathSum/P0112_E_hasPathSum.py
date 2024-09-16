# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # ref gpt
        # 檢查節點是否為空
        if not root:
            return 0
        # 檢查最後節點 
        if not root.left and not root.right:
            return targetSum == root.val
        # 前往新節點時更新目標值
        targetSum -= root.val
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)
        return left or right
