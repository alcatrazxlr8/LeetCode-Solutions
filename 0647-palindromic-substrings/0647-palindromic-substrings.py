class Solution:
    def countSubstrings(self, s: str) -> int:
        count = [0]
        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count[0] += 1
                l -= 1
                r += 1
            return
        
        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i+1)

        return count[0]