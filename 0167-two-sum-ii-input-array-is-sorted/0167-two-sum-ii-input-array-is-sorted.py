class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        hashmap = defaultdict(int)
        # ans = []
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashmap:
                return [min(i+1, hashmap[complement]+1), max(i+1, hashmap[complement]+1)]
            hashmap[numbers[i]] = i
                # ans.append(hashmap[complement]+1)
                # ans.append(i+1)
            # else:
                # hashmap[numbers[i]] = i
        # return ans
                