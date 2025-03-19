class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(row, col):
            if (row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0"):
                return

            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)
            

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = "0"
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ( rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # bfs(i, j)
                    islands += 1
        return islands