class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(curr, rem):
            if not rem:
                res.append(curr.copy())
                return
            
            for i in range(len(rem)):
                curr.append(rem[i])
                helper(curr, rem[:i]+rem[i+1:])
                curr.pop()
                
        helper([], nums)
        return res
        