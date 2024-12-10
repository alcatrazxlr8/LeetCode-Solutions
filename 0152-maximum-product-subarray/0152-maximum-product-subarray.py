class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxProd = -99999999999
        pre = suf = 1
        for i in range(n):
            if pre == 0: pre = 1
            if suf == 0: suf = 1
            pre *= nums[i]
            suf *= nums[n-i-1]
            maxProd = max(maxProd, pre, suf)

        return maxProd