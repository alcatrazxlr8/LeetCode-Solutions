class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(2, len(nums)):
            if nums[r-2] + nums[r] == nums[r-1]/2:
                ans += 1
            # l += 1
        return ans