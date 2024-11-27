class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def getMax(nums):
            prev, curr = 0, 0
            for n in nums:
                tmp = max(n+prev, curr)
                prev = curr
                curr = tmp
            return curr
        return max(getMax(nums[:-1]), getMax(nums[1:]))