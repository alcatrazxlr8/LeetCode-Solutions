# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs = []
        q = deque([root])
        
        while q:
            qLen = len(q)
            levels = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                bfs.append(levels)
        ans = []
        for i in bfs:
            ans.append(i[-1])
            
        return ans
            