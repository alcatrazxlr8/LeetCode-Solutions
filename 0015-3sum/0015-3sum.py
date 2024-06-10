class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if (nums[i] + nums[l] + nums[r] == 0):
                    trip = [nums[i], nums[l], nums[r]]
                    # trip.sort()
                    trip = tuple(trip)
                    ans.add(trip)
                    l += 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1
        return ans