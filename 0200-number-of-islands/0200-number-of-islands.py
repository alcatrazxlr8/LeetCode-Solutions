class Solution:

    def dfs(self, grid, i, j, visited):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == "0" or visited[(i,j)] == 1):
            return
        visited[(i,j)] = 1
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j-1, visited)
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i, j+1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])

        visited = {}
        
        for i in range(m):
            for j in range(n):
                visited[(i,j)] = 0
                
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1" and visited[(i,j)] != 1):
                    self.dfs(grid, i, j, visited)
                    islands += 1
                # visited[i][j] = 1
            
        return islands