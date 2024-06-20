class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        ans = 0
        while (r < len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            r = r+1    
            ans = max(ans, profit)

        return ans
                