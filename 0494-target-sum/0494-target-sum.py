class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        ## MEMOIZATION 
        dp = {}
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            add = dfs(i+1, total+nums[i])
            
            sub = dfs(i+1, total-nums[i])

            dp[(i, total)] = add + sub

            return dp[(i, total)]
        return dfs(0, 0)


        # ## Backtracking (TLE)
        # def backtrack(i, total):
        #     if i == len(nums):
        #         return total == target

        #     add = backtrack(i+1, total + nums[i])
        #     sub = backtrack(i+1, total - nums[i])

        #     return add + sub
        # return backtrack(0, 0)
        
        