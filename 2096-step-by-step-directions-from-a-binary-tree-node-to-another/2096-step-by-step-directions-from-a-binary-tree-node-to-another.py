# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def lowestCommonAncestor(self, root, p, q):
        if (root == None or root.val == p or root.val == q):
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l if l else r

    def search(self, root, target, path):
        if not root:
            return False
        if root.val == target:
            return True
        path.append('L')
        if self.search(root.left, target, path):
            return True
        path.pop()
        path.append('R')
        if self.search(root.right, target, path):
            return True
        path.pop()
        return False
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        lca = self.lowestCommonAncestor(root, startValue, destValue)
        
        pathToRoot = []
        pathFromRoot = []        
        
        self.search(lca, startValue, pathToRoot)
        self.search(lca, destValue, pathFromRoot)
        
        pathToRoot = ['U'] * len(pathToRoot)
        
        return ''.join(pathToRoot) + ''.join(pathFromRoot) 
        
            ## We find path from start to lca and then lca to dest 
            #### lca to dest can be done by searching but how do we go up for start to lca
            ###### so we reverse 
            
            
            
            