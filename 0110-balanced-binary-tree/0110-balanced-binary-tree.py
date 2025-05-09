# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [0, True]
            l = dfs(root.left)
            r = dfs(root.right)
            diff = abs(r[0]-l[0])

            return [1 + max(l[0], r[0]), l[1] and r[1] and diff <= 1]

        return dfs(root)[1]

        
