class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = {}
        ans = []
        for i in range(1, (n**2)+1):
            nums[i] = 1
        for i in range(n):
            for j in range(n):
                if nums[grid[i][j]] == 0: ## repeated
                    ans.append(grid[i][j])
                else:
                    nums[grid[i][j]] -= 1
        for num, count in nums.items():
            if count == 1: ## missing
                ans.append(num)

        return ans