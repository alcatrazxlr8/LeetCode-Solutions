class Solution:
    def totalNQueens(self, n: int) -> int:
        
        if n == 1:
            return 1
        elif n == 2 or n == 3:
            return 0

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
                count[0] += 1
                return
                
            for row in range(n):
                if canFill(grid, row, col):
                    grid[row][col] = "Q"
                    rec(col + 1, grid)
                    grid[row][col] = "."
        
        count = [0]
        rec(0, grid)
        return count[0]