# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
                return False
        def isMirror(left:TreeNode,right:TreeNode) ->bool:
            # 檢查最底層
            if not left and not right:
                return True 
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(right.left,left.right)
            
        return isMirror(root.left, root.right)