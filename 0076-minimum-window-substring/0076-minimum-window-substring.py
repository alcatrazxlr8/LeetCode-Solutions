class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        count_t = Counter(t)
        window_count = {} #Counter()
        have = 0 ## num of distinct chars that our window satisfies
        req = len(count_t) ## num of distinct chars in "t"
        min_sub = (float('inf'), None, None)
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window_count[char] = 1 + window_count.get(char, 0)

            if char in count_t and window_count[char] == count_t[char]:
                have += 1

            while l <= r and have == req:
                if r-l+1 < min_sub[0]:
                    min_sub = (r-l+1, l, r)

                window_count[s[l]] -= 1
                if s[l] in count_t and window_count[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        if min_sub[0] == float('inf'):
            return ""
        else:
            return s[min_sub[1]: min_sub[2]+1]
