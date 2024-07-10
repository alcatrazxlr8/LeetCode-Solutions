class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1
        
        while(left <= right):
            mid = left + int((right - left)/2)
            # midRow = math.ceil(mid/cols) - 1
            midRow = mid // cols
            midCol = mid % cols
            
            
            # print(matrix[midRow][midCol])
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            elif matrix[midRow][midCol] < target:
                left = mid + 1
                
        return False
            