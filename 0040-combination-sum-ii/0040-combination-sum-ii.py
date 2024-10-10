# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         # candidates = set(candidates)
#         # candidates = list(candidates)
#         ans = []
#         n = len(candidates)
        
#         def rec(i, target, arr):

#             if i == n:
#                 if target == 0:
#                     ans.append(arr.copy())
#                 return
            
#             if candidates[i] <= target:
#                 arr.append(candidates[i])
#                 rec(i+1, target-candidates[i], arr)
#                 arr.pop()
#             rec(i+1, target, arr)

#         rec(0, target, [])
#         for i in ans:
#             i.sort()
#             print (i)
#         # print(ans)
#         return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(candidates)
        candidates.sort() ### sorted to handle dupes

        def rec(i, target, arr):
            if target == 0:
                ans.append(arr.copy()) 
                return
            
            # if i == n or candidates[i] > target:
            #     return
            for j in range(i, n):
                # Skip duplicates
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[i] > target:
                    break
                arr.append(candidates[j])
                rec(j + 1, target - candidates[j], arr) 
                arr.pop()

        rec(0, target, [])
        return ans
