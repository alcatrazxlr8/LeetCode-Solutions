# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         m = len(heights)
#         n = len(heights[0])
        
#         aq = deque()
#         pq = deque()
        
#         # aVis = {}
#         # pVis = {}
#         aVis = [[0] * n for _ in range(m)]
#         pVis = [[0] * n for _ in range(n)]
        
#         for i in range(m):
#             aq.append([i, n-1])
#             aVis[i][n-1] = 1
#             pq.append([i, 0])
#             pVis[i][0] = 1
            
#         for j in range(n):
#             aq.append([m-1, j])
#             aVis[m-1][j] = 1
#             pq.append([0, j])
#             pVis[0][j] = 1
            
#         def bfs(q, vis):
            
#             directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             while q:
#                 row, col = q.popleft()
#                 for dr, dc in directions:
#                     r = row + dr
#                     c = col + dc
#                     if 0 <= r < m and 0 <= c < n and not vis[r][c]:
#                         if heights[r][c] >= heights[row][col]:
#                             vis[r][c] = 1
#                             q.append([r, c])
                            
#         bfs(aq, aVis)
#         bfs(pq, pVis)
        
#         res = []
        
#         for i in range(m):
#             for j in range(n):
#                 if aVis[i][j] and pVis[i][j]:
#                     res.append([i, j])
                    
#         return res
        
                
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        aq = deque()
        pq = deque()
        
        aVis = [[False] * n for _ in range(m)]
        pVis = [[False] * n for _ in range(m)]
        
        for i in range(m):
            aq.append((i, 0))
            aVis[i][0] = True
            pq.append((i, n-1))
            pVis[i][n-1] = True
            
        for j in range(n):
            aq.append((0, j))
            aVis[0][j] = True
            pq.append((m-1, j))
            pVis[m-1][j] = True
            
        def bfs(q, vis):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < m and 0 <= c < n and not vis[r][c]:
                        if heights[r][c] >= heights[row][col]:
                            vis[r][c] = True
                            q.append((r, c))
                            
        bfs(aq, aVis)
        bfs(pq, pVis)
        
        res = []
        
        for i in range(m):
            for j in range(n):
                if aVis[i][j] and pVis[i][j]:
                    res.append([i, j])
                    
        return res
