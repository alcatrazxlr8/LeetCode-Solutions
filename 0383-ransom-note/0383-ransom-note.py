class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        big = Counter(magazine)
        small = Counter(ransomNote)

        return big & small == small

        # for key, value in small.items():
        #     if big[key] < value or not big[key]:
        #         return False
        # return True