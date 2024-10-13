class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def rec(i, nums, ans):
            if i == len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[i])
            rec(i+1, nums, ans)
            ans.pop()
            rec(i+1, nums, ans)
            
        res = []
        rec(0, nums, [])
        return res