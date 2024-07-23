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
            for child in root.children:
                self.trav(child, ans)
            ans.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.trav(root, ans)
        return ans
