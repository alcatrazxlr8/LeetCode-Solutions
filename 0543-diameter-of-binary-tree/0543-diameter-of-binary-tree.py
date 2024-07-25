# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ans = 0
        
    def dfs(self, root):
        if not root:
            return -1
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans = max(self.ans, 2 + l + r)
        return 1 + max(l, r)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans