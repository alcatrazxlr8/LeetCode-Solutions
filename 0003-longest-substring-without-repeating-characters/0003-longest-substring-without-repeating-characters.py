class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        seen = set()
        while(r<len(s)):
            if s[r] in seen:
                while(s[l] != s[r]):
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[r])
                ans = max(ans, len(seen))
            r += 1
        return ans
        
                
                
            
                
        