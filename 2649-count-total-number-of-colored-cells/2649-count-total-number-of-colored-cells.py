class Solution:
    def coloredCells(self, n: int) -> int:
        
        # 1 + 4(1) + 4(2) + 4(3) + 4(4) + .....
        # 1 + 4 (1 + 2 + 3 + 4 + 5 + .....)
        # 1 + 4(n*(n-1)/2)
        return 1 + 2*n*(n-1)


        
        # ans = [0]*n
        # ans[0] = 1
        # for i in range(1, n):
        #     ans[i] = ans[i-1] + 4*i
        # return ans[n-1]