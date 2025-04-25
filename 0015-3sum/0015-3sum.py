class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ## now we find 2 sum with target
            # sol = [nums[i]]
            target = -nums[i]
            complements = {}
            for j in range(i+1, len(nums)):
                complement = target - nums[j]
                if complement in complements:
                    # sol = sol + [nums[j], complement]
                    triplet = [nums[i], nums[j], complement]
                    ans.add(tuple(sorted(triplet)))
                complements[nums[j]] = complement
        
        return list(ans)