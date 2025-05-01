class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] > target or target> nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            ## right sorted
            else:
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1