# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p and q:
            if (p.val != q.val):
                return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or (root and not subRoot):
            return True
        if (not root and subRoot):
            return False
        if (root and subRoot):
            if (root.val != subRoot.val):
                    return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            else:
                if self.isSameTree(root, subRoot):
                    return self.isSameTree(root, subRoot)
                else:
                    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        
        return False
                
                
            
        
        
        
        
        
        # if (not root and not subRoot):
        #     return True
        # if (not root and subRoot) or (root and not subRoot):
        #     return False
        # # if root and subRoot:
        # # if (root.val == subRoot.val):
        # else:
        #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # return True