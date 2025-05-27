# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, res)
        return res[k-1]

        # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:         
        #     res = []
        #     def dfs(root):
        #         if not root:
        #             return
        #         dfs(root.left)
        #         heapq.heappush(res, root.val)
        #         dfs(root.right)
            
        #     dfs(root)
        #     while k > 0:
        #         tmp = heapq.heappop(res)
        #         k -= 1
        #     return tmp