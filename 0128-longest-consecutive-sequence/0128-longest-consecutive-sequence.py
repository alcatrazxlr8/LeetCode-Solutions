class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if (num-1) not in nums:
                seq = 0
                while (num+seq) in nums:
                    seq += 1
                    ans = max(ans, seq)
            else:
                continue
        return ans