# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, mx):
            if root==None:
                return 0
            t = 1 
            if mx>root.val:
                t = 0 
            if t==1: print(root.val) 
            return t+traverse(root.left, max(mx, root.val))+traverse(root.right, max(mx, root.val))
        return traverse(root, root.val)