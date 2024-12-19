class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]
        if color == startColor:
            return image
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != startColor:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            # if r >= 0 and r < rows and c >= 0 and c < cols and image[r][c] == startColor:
                # if image[r][c] == startColor:
                # image[r][c] = color
                # dfs(r+1, c)
                # dfs(r, c+1)
                # dfs(r-1, c)
                # dfs(r, c-1)
        dfs(sr, sc)
        return image