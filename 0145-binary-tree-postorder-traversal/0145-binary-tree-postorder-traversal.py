# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def trav(root):
            if root:
                trav(root.left)
                trav(root.right)
                ans.append(root.val)
                
        trav(root)
        return ans