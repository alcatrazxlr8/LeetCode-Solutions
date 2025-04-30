class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low_row = 0
        high_row = m - 1
        while low_row <= high_row:
            mid_row = low_row + (high_row - low_row)//2
            if matrix[mid_row][0] <= target <= matrix[mid_row][n-1]:
                ## binary search in this row again
                l = 0
                r = n-1
                while l <= r:
                    mid = l + (r-l)//2
                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False

            elif target < matrix[mid_row][0]:
                high_row = mid_row - 1
            elif target > matrix[mid_row][n-1]:
                low_row = mid_row + 1
        return False
