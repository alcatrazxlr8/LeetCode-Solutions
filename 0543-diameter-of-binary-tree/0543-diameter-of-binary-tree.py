# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)     
            right = dfs(root.right)     
            depth = max(left, right) + 1
            dia[0] = max(dia[0], left + right)
            return depth
        dfs(root)
        return dia[0]
