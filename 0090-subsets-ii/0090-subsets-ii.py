class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        n = len(nums)
        
        def rec(i, arr):
            ans.append(arr.copy())
            for j in range(i, n):
                if j != i and nums[j] == nums[j - 1]:
                    continue
                arr.append(nums[j])
                rec(j + 1, arr)
                arr.pop()
                
        rec(0, [])
        return ans