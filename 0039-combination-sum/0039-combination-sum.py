class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates)
        
        def rec(i, target, arr):

            if i == n:
                if target == 0:
                    ans.append(arr.copy())
                return
            if candidates[i] <= target:
                arr.append(candidates[i])
                rec(i, target-candidates[i], arr)
                arr.pop()
            rec(i+1, target, arr)

        rec(0, target, [])
        return ans