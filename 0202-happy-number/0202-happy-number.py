class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            res = 0
            while n:
                digit = n % 10
                res += digit**2
                n = n // 10
            return res 

        visited = set()
        while n not in visited:
            visited.add(n)
            n = getNext(n)
            if n == 1:
                return True
        return False
        