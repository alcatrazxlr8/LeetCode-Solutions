class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_s = filter(lambda x: x.isalnum(), s)
        clean_s = "".join(clean_s)
        left = 0
        right = len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            right -= 1
            left += 1
        return True