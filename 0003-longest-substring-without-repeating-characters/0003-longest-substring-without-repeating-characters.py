class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        a   b   c   a   b   c   b   b
        ^   ^
        '''

        l = 0
        r = 0
        currSet = set()
        ans = 0
        while r < len(s):
            if s[r] in currSet:
                while s[r] in currSet:
                    currSet.remove(s[l])

                    l += 1
            else:
                currSet.add(s[r])
                ans = max(ans, r-l+1)
                r += 1

        return ans
            