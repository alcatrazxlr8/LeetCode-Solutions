# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialized(root):
            if not root:
                return "#"
            return f"({root.val},{serialized(root.left)},{serialized(root.right)})"
        rootSer = serialized(root)
        subrootSer = serialized(subRoot)
        return subrootSer in rootSer