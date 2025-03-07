class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target =  -nums[i]
            
            while left < right:
                if nums[left] + nums[right] == target:
                    trip = [nums[i], nums[left], nums[right]]
                    trip = tuple(trip)
                    ans.add(trip)
                    left += 1
                    # while nums[left] == nums[left-1] and left < right:
                    #     left +=1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(ans)
