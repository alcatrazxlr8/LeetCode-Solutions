class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[inf for _ in range(n)] for _ in range(m)]

        ## 1st pass (top to bottom)
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    ans[row][col] = 0
                else:
                    if row > 0:
                        ans[row][col] = min(ans[row][col], ans[row-1][col] + 1)
                    if col > 0:
                        ans[row][col] = min(ans[row][col], ans[row][col-1] + 1)
                        
        ## 2nd pass (bottom to top)                
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row < m-1:
                    ans[row][col] = min(ans[row][col], ans[row+1][col] + 1)
                if col < n-1:
                    ans[row][col] = min(ans[row][col], ans[row][col+1] + 1)

        return ans