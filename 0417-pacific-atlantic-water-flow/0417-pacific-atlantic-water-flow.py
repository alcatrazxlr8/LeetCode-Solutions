class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        def bfs(ocean):
            visited = set(ocean)
            q = deque(ocean)

            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and (row,col) not in visited and heights[row][col] >= heights[r][c]:
                        visited.add((row, col))
                        q.append([row, col])
            return visited

        pacific = [(x, 0) for x in range(ROWS)]+[(0, y) for y in range(COLS)]
        atlantic = [(x, COLS-1) for x in range(ROWS)]+[(ROWS-1, y) for y in range(COLS)]

        pacific = bfs(pacific)
        atlantic = bfs(atlantic)
        intersection = pacific & atlantic
        
        res = [[r, c] for r, c in intersection]
        return res
