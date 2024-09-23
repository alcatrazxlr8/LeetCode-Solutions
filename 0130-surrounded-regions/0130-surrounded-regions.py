class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            board[r][c] = "U"
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        rows = len(board)
        cols = len(board[0])
        
        if rows <= 2 or cols <= 2:
            return
        
        visited = {}
        edge = []
        for i in range(rows):
            if board[i][0] == "O":
                edge.append([i, 0])
            if board[i][cols - 1] == "O":
                edge.append([i, cols - 1])
                
        for j in range(cols):
            if board[0][j] == "O":
                edge.append([0, j])
            if board[rows - 1][j] == "O":
                edge.append([rows - 1, j])
                
        for region in edge:
            r, c = region[0], region[1]
            dfs(r, c)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "U":
                    board[r][c] = "O"