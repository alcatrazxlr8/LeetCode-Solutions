class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def anagram(s, t):
            sortedS = sorted(s)
            sortedT = sorted(t)
            return sortedS == sortedT
            
        left = 0
        for i in range(len(s2) - len(s1) + 1):
            
            if anagram(s1, s2[left:left+len(s1)]):
                return True
            left += 1
            
        return False
            
            
                