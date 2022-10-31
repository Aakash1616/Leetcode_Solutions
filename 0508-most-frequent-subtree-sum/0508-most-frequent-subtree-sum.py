# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def trav(root):
            if not root:
                return 0 
            l = trav(root.left) 
            r = trav(root.right) 
            dic[root.val+l+r]+=1 
            return l+r+root.val 
        dic = defaultdict(lambda : 0)
        trav(root) 
        mx = max(dic[i] for i in dic)
        res = []
        for i in dic:
            if dic[i]==mx:
                res.append(i) 
        return res 