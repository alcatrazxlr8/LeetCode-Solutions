class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxLen = 0
        count = defaultdict(int)
        
        for right in range(len(s)):
            # if(k)
            count[s[right]] += 1
            while ((right - left + 1) - max(count.values()) > k):
                count[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen