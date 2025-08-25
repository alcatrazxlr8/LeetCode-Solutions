class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minCol = COLS-1
        minRow = ROWS-1
        maxCol = 0
        maxRow = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    minCol = min(minCol, c)
                    minRow = min(minRow, r)
                    maxCol = max(maxCol, c)
                    maxRow = max(maxRow, r)

        minArea = (maxRow - minRow + 1) * (maxCol - minCol + 1)

        return minArea
