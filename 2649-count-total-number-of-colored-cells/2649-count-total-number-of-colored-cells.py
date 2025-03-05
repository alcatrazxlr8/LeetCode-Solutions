class Solution:
    def coloredCells(self, n: int) -> int:
        ans = [0]*n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i-1] + 4*i
        return ans[n-1]