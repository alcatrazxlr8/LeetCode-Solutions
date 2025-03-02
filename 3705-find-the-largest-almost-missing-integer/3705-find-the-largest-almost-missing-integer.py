class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # ans = -1
        # left = 0
        # right = k-1
        # while right < len(nums):

        n = len(nums)
        if k == n:
            return max(nums)
        if n == 1:
            return nums[0]
        unique = []
        count = Counter(nums)
        for key, value in count.items():
            if value == 1:
                unique.append(key)
                
        if k == 1 and unique:
            ## find non-repeating nums
                ## return max from those
            # if unique:
            return max(unique)
        else:
            tmp = -1
            ## check if nums[0] or nums[-1] repeat
                ## return max of the non-repeating from both
            if nums[0] not in nums[1:]:
                tmp = nums[0]
            if nums[-1] not in nums[0:n-1]:
                tmp = max(tmp, nums[-1])

            if tmp >=0:
                return tmp

        return -1