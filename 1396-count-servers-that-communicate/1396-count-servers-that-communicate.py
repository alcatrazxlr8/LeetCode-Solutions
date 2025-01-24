class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1):
                    count +=1

        return count