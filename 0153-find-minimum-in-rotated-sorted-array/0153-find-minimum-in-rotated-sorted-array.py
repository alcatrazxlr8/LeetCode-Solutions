class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 9999999
        if(nums[left] < nums[right]):
            return nums[left]
        while(left <= right):
            
            mid = left + int((right-left)/2)
            if left == mid == right:
                return nums[left]
            
            if nums[mid] < nums[right]:
                ans = min(ans, nums[mid])
                right = mid
            else:
                ans = min(ans, nums[right])
                left = mid + 1
            
        return ans