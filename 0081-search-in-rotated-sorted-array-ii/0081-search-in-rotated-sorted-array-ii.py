class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True

            ## the only case where we'll have problems
            if nums[mid] == nums[low] == nums[high]:
                low += 1
                high -= 1
                continue
            ## left sorted
            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            ## right sorted
            else:
                if nums[mid] <= nums[high]:
                    if nums[mid] <= target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1

        return False
