class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []
        
        def isPalindrome(s, start, end):
            while(start <= end):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
            
        def rec(s, index):
            if index == len(s):
                res.append(path.copy())
                return
            
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index : i + 1])
                    rec(s, i + 1)
                    path.pop()
                    
        rec(s, 0)
        return res
            