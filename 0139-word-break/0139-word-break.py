class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

    #     # # RECURSIVE (TLE)
    #     # def rec(i):
    #     #     if i == len(s):
    #     #         return True
    #     #     for word in wordDict:
    #     #         if ((i+len(word) <= len(s)) and s[i:i+len(word)] == word):
    #     #             if rec(i+len(word)):
    #     #                 return True
    #     #     return False
        
    #     # return rec(0)