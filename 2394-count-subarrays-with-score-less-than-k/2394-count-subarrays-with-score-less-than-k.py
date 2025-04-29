class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = r = 0
        count = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum * (r-l+1) >= k:
                window_sum -= nums[l]
                l += 1
            count += r-l+1
        return count
                
            
