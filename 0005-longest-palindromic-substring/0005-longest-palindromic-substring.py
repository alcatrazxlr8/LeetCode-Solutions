class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def centerExpand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) <= 1:
            return s
        
        maxStr = ""
        
        for i in range(len(s) - 1):
            odd = centerExpand(i, i)
            even = centerExpand(i, i+1)
            
            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even
                
        return maxStr