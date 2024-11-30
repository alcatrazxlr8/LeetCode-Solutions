class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            elif i in memo:
                return memo[i]

            res = dfs(i+1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    res += dfs(i+2)
            memo[i] = res
            return memo[i]
        return dfs(0)


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