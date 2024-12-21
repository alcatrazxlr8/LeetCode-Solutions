class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        w1, w2 = len(word1), len(word2)
        dp = [[float('inf')] * (w2 + 1) for i in range(w1 + 1)]
        for i in range(w1+1):
            dp[i][w2] = w1 - i
        for j in range(w2+1):
            dp[w1][j] = w2 - j
        for i in range(w1-1, -1, -1):
            for j in range(w2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]



        # # RECURSION (TLE)
        # w1, w2 = len(word1), len(word2)

        # def dfs(i, j):
        #     # if w2 and not w1:
        #     if i == w1:
        #         return w2 - j
        #     # if w1 and not w2:
        #     if j == w2:
        #         return w1 - i
        #     # if not w1 and not w2:
        #     #     return 0
        #     if word1[i] == word2[j]:
        #         return dfs(i+1, j+1) 
        #     return 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))

        # return dfs(0, 0)