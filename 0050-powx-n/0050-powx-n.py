class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ## Binary Exponentiation [Optimal]
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        half = self.myPow(x, n//2)
        return half * half if n&1 == 0 else half * half * x
        ## TLE
        # ans = 1
        # if n == 0 or x == 1:
        #     return 1
        # if x == 0:
        #     return 0
        # if n > 0:
        #     for i in range(n):
        #         ans *= x
        # if n < 0:
        #     for i in range(abs(n)):
        #         ans = ans * 1/x

        # return ans