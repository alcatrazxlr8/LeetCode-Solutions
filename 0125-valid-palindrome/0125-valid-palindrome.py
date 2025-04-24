class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                # print(s[l], s[r])
                return False
            l += 1
            r -= 1

            # if not s[l].isalnum():
            #     l += 1
            #     # print(f"l: {l}")
            # elif not s[r].isalnum():
            #     r -= 1
            #     # print(f"r: {r}")
            # elif s[l] == s[r]:
            #     l += 1
            #     r -= 1
            # else:
            #     return False
        return True

