class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def rec(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = rec(i + 1, buying)
            if buying:
                buy = -prices[i] + rec(i + 1, not buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = prices[i] + rec(i + 2, not buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return rec(0, True)