class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        def rec():
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == '.':
                        for strNum in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if isValid(r, c, strNum):
                                board[r][c] = strNum
                                
                                if rec():
                                    return True
                                # else:
                                board[r][c] = '.'
                        return False
            return True
            
        def isValid(r, c, num):
            for i in range(rows):
                if board[i][c] == num or board[r][i] == num or board[3 * (r // 3) + (i // 3)][3 * (c // 3) + (i % 3)] == num:
                    return False
            return True
        
        rec()
        