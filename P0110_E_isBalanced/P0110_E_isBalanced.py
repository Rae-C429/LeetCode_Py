# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, balanced = self.deep(root)
        return balanced
    def deep(self,root):
        if not root:
            return 0, True
        leftHeight, leftBalance = self.deep(root.left)
        rightHeight, rightBalance = self.deep(root.right)

        currentBalance = leftBalance and rightBalance and (abs(leftHeight - rightHeight) <=1)

        return max(leftHeight,rightHeight)+1, currentBalance
             