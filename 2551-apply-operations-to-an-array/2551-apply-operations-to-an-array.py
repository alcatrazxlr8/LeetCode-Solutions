class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] != 0 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
        while p1 < len(nums):
            nums[p1] = 0
            p1 += 1
        return nums