class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # print(f"result = {result} ; num = {num} ; xor = {result ^ num}")
            # I had trouble understanding why the subsequent occurances cancelled out, 
            # but looking at the binary representation of nums and result helped clarify things
            result ^= num
        return result