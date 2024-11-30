class Solution:
    def numDecodings(self, s: str) -> int:

        ### BOTTOM UP DP - Tabulation
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[n] = 1
        if s[n-1] != '0':
            dp[n-1] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
                if (i < n-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'))):
                    dp[i] += dp[i+2]
        return dp[0]

        ### TOP DOWN DP - Memoization
        # memo = {}
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     elif i in memo:
        #         return memo[i]

        #     memo[i] = dfs(i+1)
        #     if i < len(s) - 1:
        #         if (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
        #             memo[i] += dfs(i+2)
        #     # memo[i] = res
        #     return memo[i]

        # return dfs(0)


        ### RECURSIVE - BETTER (TLE)
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
            
        #     res = dfs(i+1)
        #     if i < len(s) - 1:
        #         if (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
        #             res += dfs(i+2)
            
        #     return res

        # return dfs(0)

        
        ### RECURSIVE (TLE)
        # def rec(subStr): ## checks 
        #     if subStr == "":
        #         return 1
        #     if subStr[0] == 0:
        #         return 0
        #     res = 0
        #     if subStr[0] in "123456789":
        #         res += rec(subStr[1:])
        #     if len(subStr) >= 2 and "10" <= subStr[:2] <= "26":
        #         res += rec(subStr[2:])

        #     return res
        # return rec(s)