class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        if n == 1:
            return [["Q"]]
        elif n == 2 or n == 3:
            return []
        
        ans = []
        grid = [['.' for _ in range(n)] for _ in range(n)]
        
        def canFill(grid: List[List[str]], r: int, c: int) -> bool:
            
            ### upper diag [row, col both decreasing]
            row, col = r, c
            while(row >= 0 and col >= 0):
                if grid[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            ### left [col decreasing]
            row, col = r, c
            while col >= 0:
                if grid[row][col] == "Q":
                    return False
                col -= 1
            
            ### lower diag [col decreasing, row increasing]
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
            
            