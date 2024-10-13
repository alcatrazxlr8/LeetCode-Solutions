class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        # for i in range(n):
        #     tmp = []
        #     s = ""
        #     for j in range(n):
        #         s += "."
        #     grid.append(s)
        # ans.append(grid)
        # grid = ['.' * n for _ in range(n)]
        grid = [['.' for _ in range(n)] for _ in range(n)]
        
        
        def canFill(grid: List[List[str]], r: int, c: int) -> bool:
            
            ### upper diag
            row, col = r, c
            while(row >= 0 and col >= 0):
                if grid[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            ### left
            row, col = r, c
            while col >= 0:
                if grid[row][col] == "Q":
                    return False
                col -= 1
            
            ### lower diag
            row, col = r, c
            while col >= 0 and row < n:
                if grid[row][col] == "Q":
                    return False
                row += 1
                col -= 1
            
            return True

        def rec(col, grid):
            if col == n:
                # ans.append(grid.copy())
                ans.append([''.join(row) for row in grid])
                return
                
            for row in range(n):
                if canFill(grid, row, col):
                    grid[row][col] = "Q"
                    rec(col + 1, grid)
                    grid[row][col] = "."
        
        rec(0, grid)
        return ans
            
            