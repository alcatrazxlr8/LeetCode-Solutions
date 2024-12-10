class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -99999999999
        pre = suf = 1
        for i in range(len(nums)):
            if pre == 0: pre = 1
            if suf == 0: suf = 1
            pre = pre * nums[i]
            suf = suf * nums[len(nums)-i-1]
            maxProd = max(maxProd, pre, suf)

        return maxProd