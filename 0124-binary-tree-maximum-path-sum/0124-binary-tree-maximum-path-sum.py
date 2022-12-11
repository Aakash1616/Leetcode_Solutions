
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -float('inf')
        def subtree(node: Optional[TreeNode]) -> int:
            nonlocal mx
            if not node: return 0
            left = max(subtree(node.left), 0)
            right = max(subtree(node.right), 0)
            mx = max(mx, left + right + node.val)
            return max(
                left + node.val,
                right + node.val
            )

        subtree(root)
        return mx