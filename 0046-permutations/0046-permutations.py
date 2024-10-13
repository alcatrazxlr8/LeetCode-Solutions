class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        
        n = len(nums)
        ans = []
#         freq = [0] * n
        
#         def rec(freq, arr):
#             if len(arr) >= n:
#                 ans.append(arr.copy())
#                 return
#             for i in range(n):
#                 if not freq[i]:
#                     arr.append(nums[i])
#                     freq[i] = 1
#                     rec(freq, arr)
#                     freq[i] = 0
#                     arr.pop()
#         rec(freq, [])            

        def rec(i):
            if i >= n:
                ans.append(nums.copy())
                # print(ans)
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                rec(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        rec(0)        
        return ans
            