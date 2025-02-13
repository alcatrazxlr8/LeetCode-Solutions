class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # # sum
        # n = len(nums)
        # trueSum = n * (n+1)//2
        # currSum = sum(nums)
        # return trueSum - currSum

        
        # XOR
        ans = 0
        for i in range(1, len(nums)+1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans