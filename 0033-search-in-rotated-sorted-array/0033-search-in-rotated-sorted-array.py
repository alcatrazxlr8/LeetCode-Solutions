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
                # if target < nums[l] or target > nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    # l = mid + 1
                    r = mid - 1
                else:
                    # r = mid - 1
                    l = mid + 1
            ## right sorted portion
            else:
                # if target > nums[r] or target < nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    # r = mid - 1
                    l = mid + 1
                else:
                    # l = mid + 1
                    r = mid - 1

        return -1