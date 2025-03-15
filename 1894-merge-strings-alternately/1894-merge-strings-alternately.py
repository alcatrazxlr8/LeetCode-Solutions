class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = w2 = 0
        ans = ""
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                ans += word1[w1]
                w1 += 1
            if w2 < len(word2):
                ans += word2[w2]
                w2 += 1
        return ans