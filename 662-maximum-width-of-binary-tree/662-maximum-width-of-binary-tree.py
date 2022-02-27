# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0),]
        res = 1
        while q:
            next_q, mn, mx = [], float('inf'), 0
            for node, i in q:
                mn, mx = min(mn, i), max(mx, i)
                if node.left: next_q.append((node.left, i * 2 + 1))
                if node.right: next_q.append((node.right, i * 2 + 2))
            res = max(res, mx - mn + 1)
            q = next_q
        return res