class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def centerExpand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for i in range(len(s)):
            count += centerExpand(i, i)
            count += centerExpand(i, i+1)
            
        return count