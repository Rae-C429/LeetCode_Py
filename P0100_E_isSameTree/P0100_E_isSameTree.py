# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ref gpt
        # 如果兩個節點都為空，返回 True
        if (not p) and (not q):
            return True
        # 如果其中一個節點為空，另一個不是，返回 False
        if (not p) or (not q):
            return False
         # 如果兩個節點的值不相等，返回 False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)