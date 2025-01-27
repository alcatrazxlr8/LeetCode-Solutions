class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        zeroRows = set()
        zeroCols = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeroRows.add(row)
                    zeroCols.add(col)
        for col in zeroCols:
            for row in range(rows):
                matrix[row][col] = 0
        for row in zeroRows:
            for col in range(cols):
                matrix[row][col] = 0

        