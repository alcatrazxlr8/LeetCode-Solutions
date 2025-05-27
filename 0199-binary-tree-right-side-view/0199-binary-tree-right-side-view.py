# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        q.append(root)

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                ans.append(level)
        right = []
        for level in ans:
            right.append(level[-1])

        return right