# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root);
    def check(self, l, r):
        if not l and not r: return True 
        if l and r and l.val==r.val: 
            return self.check(l.left, r.right) and self.check(l.right, r.left)
        return False 