class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        ans = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1

            while count == k:
                ans += len(nums) - r  ## once we have reqd num of K, we add the remaining num of elements at the end after "r" since subarrays with those eles will also be valid
                if nums[l] == max_num:
                    count -= 1
                l += 1

        return ans
        