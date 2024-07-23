# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def trav(self, root, ans):
        if root:
            ans.append(root.val)
            self.trav(root.left, ans)
            self.trav(root.right, ans)
        
        return ans
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        return self.trav(root, ans)
#         ans = []
        
#         def trav(root):
#             if root:
#                 ans.append(root.val)
#                 trav(root.left)
#                 trav(root.right)
                
#         trav(root)
#         return ans