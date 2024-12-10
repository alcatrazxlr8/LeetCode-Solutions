class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]
        for num in nums[1:]:
            
            maxProd, minProd = max(maxProd*num, minProd*num, num), min(maxProd*num, minProd*num, num)
            res = max(res, maxProd)

        return res