"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def trav(self, root, ans):
        if root:
            ans.append(root.val)
            for child in root.children:
                self.trav(child, ans)

    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.trav(root, ans)
        return ans