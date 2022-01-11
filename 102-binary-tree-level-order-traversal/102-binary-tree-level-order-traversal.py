# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        queue , res = deque(), []
        queue.append(root)
        while(queue):
            lvl = []
            
            for i in range(len(queue)):
                p = queue.popleft()
                lvl.append(p.val)
            
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            res.append(lvl)
        return res
        