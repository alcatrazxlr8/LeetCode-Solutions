class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        # rotten = []
        fresh, mins = 0, 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            mins += 1
        return mins if fresh == 0 else -1
                            
            # curr = q.pop(0)
            # mins += 1
            # currX, currY = curr[0], curr[1]
            # children = [(currX + 1, currY),(currX - 1, currY),(currX, currY + 1),(currX, currY - 1)]
            # for child in children:
            #     if 0 < child[0] < n and 0 < child[1] < m:
            #         if grid[child[0]][child[1]] == 1:
            #             grid[child[0]][child[1]] = 2
            #             q.add((child[0], child[1]))
        
        
        